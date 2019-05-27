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
from keras.models import load_model


np.set_printoptions(threshold=sys.maxsize)
pd.get_option("display.max_rows", 1000)
pd.set_option('display.max_columns', 1000)

wikiSource			= 'enwiki'
answerData			= 'aesASAD3.csv'
questionData		= 'qes.csv'
dirData				= cwd+'/data/'
corpusInput			= wikiSource+'.bz2'
wikiOutput			= wikiSource+'.txt'
fileExtension		= 'bin'
trainingAlgoritm	= 0
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


crossVal = KFold(n_splits=2, random_state=True, shuffle=True)
count = 1

for dx, dy in crossVal.split(dAnswer):

	trainSAnswer = []
	trainTAnswer = []
	testSAnswer = []
	testTAnswer = []
	
	print("\n--------Fold {}--------\n".format(count))
	train, test= dAnswer.iloc[dx], dAnswer.iloc[dy]
	
	
	xtrain = train.loc[:,['Answer', 'TrueAnswer']]
	xtest = test.loc[:,['Answer', 'TrueAnswer']]
	ytrain = train.loc[:,['Score']].values
	ytest = test.loc[:,['Score']].values
	
	# bagian ini biar universal aja.
	
	[trainSAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= True)) for a1 in xtrain.loc[:,['Answer']].values]
	[trainTAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= True)) for a1 in xtrain.loc[:,['TrueAnswer']].values]
	[testSAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= True)) for a1 in xtest.loc[:,['Answer']].values]
	[testTAnswer.append(toWordList().sentenceToWordList(a1[0], changeNumber2Word= True)) for a1 in xtest.loc[:,['TrueAnswer']].values]
	
	vtrainSAnswer, vtrainTAnswer = toVectore(essays = trainSAnswer, trueAnswer=trainTAnswer, model = model, numFeature= numDimension, average=False, distance=True).changeToVector()
	vtestSAnswer, vtestTAnswer = toVectore(essays = testSAnswer, trueAnswer=testTAnswer, model = model, numFeature= numDimension, average=False, distance=True).changeToVector()
	modelNetwork = modelLSTM().biSiamenseModel(inputD=(vtrainSAnswer.shape[1], vtrainSAnswer.shape[2]))
	modelNetwork.fit([vtrainSAnswer, vtrainTAnswer], ytrain, batch_size=100, epochs=30)
	pred = modelNetwork.predict([vtestSAnswer, vtestTAnswer])

dfa = pd.DataFrame()
dfa.insert(0,'actual',ytest.flatten())
dfa.insert(1,'roundpredict',np.around(pred).flatten())
dfa.insert(2,'predict',pred.flatten())
kappa = cohen_kappa_score(ytest, np.around(pred), weights='quadratic')
mse = mean_squared_error(ytest, np.around(pred))
mae = mean_absolute_error(ytest, np.around(pred))

print(kappa);
print(mse);
print(mae);