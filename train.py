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
import gensim

wikiSource			= 'idwiki'
answerData			= 'DataAnswerExam_SMP.csv'
questionData		= 'DataQuestionExam_SMP.csv'
dirData				= cwd+'/data/'
corpusInput			= wikiSource+'.bz2'
wikiOutput			= wikiSource+'.txt'
trainingAlgoritm	= 0
numDimension		= 200
modelOutput			= wikiSource+'_word2vec_'+str(numDimension)+'_'+str(trainingAlgoritm)+'.model'


dAnswer, dQuestion = importData(answer= dirData+answerData, question= dirData+questionData).openData()

studentAnswer = []
trueAnswer = []
for a1 in dQuestion.loc[:,['Answer']].values:
	trueAnswer.append(toWordList().sentenceToWordList(a1[-1], changeNumber2Word= True))

for a1 in dAnswer.loc[:,['Answer']].values:
	studentAnswer.append(toWordList().sentenceToWordList(a1[-1], changeNumber2Word= True))

# make model
if not(os.path.exists(dirData+modelOutput)):
	if not(os.path.exists(dirData+wikiOutput)):
		steamingWiki(corpusInput=corpusInput, wikiOutput=wikiOutput).execute()
	makeModelGensim(wikiOutput=wikiOutput, modelOutput=modelOutput, numDimension=numDimension, trainingAlgoritm=trainingAlgoritm).execute()

# model = gensim.models.word2vec.Word2Vec.load(dirData+modelOutput)
data = toVectore(essays = trueAnswer, model = gensim.models.KeyedVectors.load_word2vec_format(dirData+modelOutput), numFeature= numDimension).changeToVector()
# file.write(str(data))