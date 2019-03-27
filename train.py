import os
import io
import sys
cwd = os.getcwd()
sys.path.insert(0, cwd)
from module.importData import importData
from module.toWordList import toWordList
from module.steamingWiki import steamingWiki
from module.makeModelGensim import makeModelGensim
from module.toVectore import toVectore
from module.modelLSTM import modelLSTM
from sklearn.cross_validation import KFold
from sklearn.metrics import mean_squared_error
from sklearn.metrics import cohen_kappa_score
import pandas as pd
import numpy as np
import gensim

wikiSource			= 'idwiki'
answerData			= 'DataAnswerExam_SMP.csv'
questionData		= 'DataQuestionExam_SMP.csv'
dirData				= cwd+'/data/'
corpusInput			= wikiSource+'.bz2'
wikiOutput			= wikiSource+'.txt'
fileExtension		= 'bin'
trainingAlgoritm	= 1
numDimension		= 200
modelOutput			= wikiSource+'_word2vec_'+str(numDimension)+'_'+str(trainingAlgoritm)+'.'+fileExtension


dAnswer, dQuestion = importData(answer= dirData+answerData, question= dirData+questionData).openData()

if not(os.path.exists(dirData+modelOutput)):
	if not(os.path.exists(dirData+wikiOutput)):
		steamingWiki(corpusInput=corpusInput, wikiOutput=wikiOutput).execute()
	makeModelGensim(wikiOutput=wikiOutput, modelOutput=modelOutput, numDimension=numDimension, trainingAlgoritm=trainingAlgoritm).execute()

if fileExtension != 'bin':
	model = gensim.models.word2vec.Word2Vec.load(dirData+modelOutput)
else:
	model = gensim.models.KeyedVectors.load_word2vec_format(dirData+modelOutput, unicode_errors='ignore')

msea =[]
kappa = []
for x in dQuestion.loc[:,'Essay_id'].values:
	xdAnswer = dAnswer.loc[dAnswer['Essay_id'] == x]
	xdQuestion = dQuestion.loc[dQuestion['Essay_id'] == x]

	crossVal = KFold(len(xdAnswer), n_folds=5, shuffle=True)
	results = []
	resultaa = []
	count = 1
	for dx, dy in crossVal:
		trainStudentAnswer = []
		testStudentAnswer = []
		trueAnswer = []
		
		print("\n--------Fold {}--------\n".format(count))
		train, test= xdAnswer.iloc[dx], xdAnswer.iloc[dy]
		
		xtrain = train.loc[:,['Answer']]
		xtest = test.loc[:,['Answer']]
		ytrain = train.loc[:,['Score']]
		ytest = test.loc[:,['Score']]
		
		[trainStudentAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= True)) for a1 in xtrain.values]
		[testStudentAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= True)) for a1 in xtest.values]
		[trueAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= True)) for a1 in xdQuestion.loc[:,['Answer']].values]


		dataAnswerXTrain = toVectore(essays = trainStudentAnswer, model = model, numFeature= numDimension).changeToVector()
		dataAnswerXTest = toVectore(essays = testStudentAnswer, model = model, numFeature= numDimension).changeToVector()
		dataTrueAnswer = toVectore(essays = trueAnswer, model = model, numFeature= numDimension).changeToVector()

		dataAnswerXTrain = np.reshape(dataAnswerXTrain, (dataAnswerXTrain.shape[0], 1, dataAnswerXTrain.shape[1]))
		dataAnswerXTest = np.reshape(dataAnswerXTest, (dataAnswerXTest.shape[0], 1, dataAnswerXTest.shape[1]))
		dataTrueAnswer = np.reshape(dataTrueAnswer, (dataTrueAnswer.shape[0], 1, dataTrueAnswer.shape[1]))

		modelNetwork = modelLSTM().getModel()

		print(modelNetwork)
		modelNetwork.fit(dataAnswerXTrain, ytrain, batch_size=64, epochs=50)
		ypred = modelNetwork.predict(dataAnswerXTest)
		modelNetwork.save(dirData+'model/lstm_model_'+str(x)+'.h5')
		result = mean_squared_error(ytest, np.around(ypred))
		results.append(result)
		
		resulta = cohen_kappa_score(ytest, np.around(ypred), weights='quadratic')

		print("Kappa Score: {}".format(resulta))
		resultaa.append(resulta)
		print(results)

		count += 1
	print("mse: ",np.around(np.array(results).mean(),decimals=4))
	print("Average Kappa score after a 5-fold cross validation: ",np.around(np.array(resultaa).mean(),decimals=4))
	msea.append(np.around(np.array(results).mean(),decimals=4))
	kappa.append(np.around(np.array(resultaa).mean(),decimals=4))

print(msea)
print(kappa)