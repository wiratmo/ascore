import os
import sys
cwd = os.getcwd()
sys.path.insert(0, cwd)
from module.importData import importData
from module.toWordList import toWordList

dirData = '/data/'

answerData = 'DataAnswerExam_SMP.csv'
questionData = 'DataQuestionExam_SMP.csv'

a, b, c, d = importData(answer= cwd+dirData+answerData, question= cwd+dirData+questionData).ExposeData()

sentences = []
for a1 in a.loc[:,['Answer']].values:
	sentences.append(toWordList().sentenceToWordList(a1[-1], changeNumber2Word= True))
print((sentences))