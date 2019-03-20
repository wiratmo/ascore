import os
import sys
cwd = os.getcwd()
sys.path.insert(0, cwd)
from module.importData import importData
from module.toWordList import toWordList
from module.steamingWiki import steamingWiki
from module.makeModelGensim import makeModelGensim

wikiSource		= 'enwiki'
answerData 		= 'DataAnswerExam_SMP.csv'
questionData 	= 'DataQuestionExam_SMP.csv'
dirData 		= cwd+'/data/'
corpusInput		= wikiSource+'.bz2'
wikiOutput		= wikiSource+'.txt'
trainingAlgoritm= 0
numDimension	= 200
modelOutput		= wikiSource+'_word2vec_'+str(numDimension)+'.model'


a, b, c, d = importData(answer= dirData+answerData, question= dirData+questionData).ExposeData()

sentences = []
for a1 in a.loc[:,['Answer']].values:
	sentences.append(toWordList().sentenceToWordList(a1[-1], changeNumber2Word= True))
# print((sentences))

if not(os.path.exists(dirData+modelOutput)):
	if not(os.path.exists(dirData+wikiOutput)):
		steamingWiki(corpusInput=corpusInput, wikiOutput=wikiOutput).execute()
	makeModelGensim(wikiOutput=wikiOutput, modelOutput=modelOutput, numDimension=numDimension, trainingAlgoritm=trainingAlgoritm).execute()
