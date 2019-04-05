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
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, mean_absolute_error, cohen_kappa_score
import pandas as pd
import numpy as np
import gensim

np.set_printoptions(threshold=sys.maxsize)

wikiSource			= 'idwiki'
# answerData			= 'DataAnswerExam_SMP.csv'
# answerData			= 'aes.csv'
answerData			= 'aesnormal.csv'
questionData		= 'DataQuestionExam_SMP.csv'
# questionData		= 'qes.csv'
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
maea =[]
kappa = []
# file = io.open("dump.txt", "w")

for x in (dQuestion.loc[:,'Essay_id'].values):
	if x in dAnswer.loc[:,'Essay_id'].values:
		xdAnswer = dAnswer.loc[dAnswer['Essay_id'] == x]
		xdQuestion = dQuestion.loc[dQuestion['Essay_id'] == x]
		crossVal = KFold(n_splits=2, random_state=None, shuffle=True)
		results = []
		resultaa = []
		resultbb = []
		count = 1

		for dx, dy in crossVal.split(xdAnswer):
			trainStudentAnswer = []
			testStudentAnswer = []
			trueAnswer = []
			question = []
			
			print("\n--------Fold {}--------\n".format(count))
			train, test= xdAnswer.iloc[dx], xdAnswer.iloc[dy]
			
			xtrain = train.loc[:,['Answer']]
			xtest = test.loc[:,['Answer']]
			ytrain = train.loc[:,['Score']].values
			ytest = test.loc[:,['Score']].values
			
			[trainStudentAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= False, question=xdQuestion.loc[:,'Question'].values[0])) for a1 in xtrain.values]
			[testStudentAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= False, question=xdQuestion.loc[:,'Question'].values[0])) for a1 in xtest.values]
			[trueAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= False, question=xdQuestion.loc[:,'Question'].values[0])) for a1 in xdQuestion.loc[:,['Answer']].values]
			
			dataAnswerXTrain, dataTrueAnswerX = toVectore(essays = trainStudentAnswer, trueAnswer=trueAnswer, model = model, numFeature= numDimension, average=False, distance=True).changeToVector()
			dataAnswerXTest, dataTrueAnswerY = toVectore(essays = testStudentAnswer, trueAnswer=trueAnswer, model = model, numFeature= numDimension, average=False, distance=True).changeToVector()
			
			modelNetworka = modelLSTM().getModel()
			modelNetworkb = modelLSTM().getModel()

			modelNetworka.fit(dataAnswerXTrain, ytrain, batch_size=100, epochs=100)
			modelNetworka.fit(dataTrueAnswerX, ytrain, batch_size=100, epochs=100)

			ypred = modelNetworka.predict(dataAnswerXTest)
			ypredb = modelNetworka.predict(dataTrueAnswerY)
			modelNetworka.save(dirData+'model/lstm_model_'+str(x)+'.h5')
			# file.write(str(ypred)+"\n")
			# file.write(str(ytest))
			result = mean_squared_error(ytest, np.around(ypred))
			resulta = cohen_kappa_score(ytest, np.around(ypred), weights='quadratic')
			resultb = mean_absolute_error(ytest, np.around(ypred))
			results.append(result)
			resultaa.append(resulta)
			resultbb.append(resultb)
			

			print("MSE :{}".format(results))
			print("Kappa Score: {}".format(resultaa))
			print("MAE :{}\n".format(resultbb))

			print("MSE :{}".format(mean_squared_error(ytest, np.around(ypredb))))
			print("Kappa Score: {}".format(cohen_kappa_score(ytest, np.around(ypredb), weights='quadratic')))
			print("MAE :{}".format(mean_absolute_error(ytest, np.around(ypred))))

			count += 1

# 		print("mse: ",np.around(np.array(results).mean(),decimals=4))
# 		print("Average Kappa score after a 5-fold cross validation: ",np.around(np.array(resultaa).mean(),decimals=4))
# 		print("mae: ",np.around(np.array(resultbb).mean(),decimals=4))
# 		msea.append(np.around(np.array(results).mean(),decimals=4))
# 		kappa.append(np.around(np.array(resultaa).mean(),decimals=4))
# 		maea.append(np.around(np.array(resultaa).mean(),decimals=4))

# print(msea)
# print(kappa)
# print(maea)