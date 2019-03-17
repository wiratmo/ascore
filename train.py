from module.importData import importData
from module.toWordList import toWordList

a, b, c, d = importData(answer='DataAnswerExam_SMP.csv', question='DataQuestionExam_SMP.csv').ExposeData()

sentences = []
for a1 in a.loc[:,['Answer']].values:
	sentences.append(toWordList().sentenceToWordList(a1[-1], changeNumber2Word= True))
print((sentences))