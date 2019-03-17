from module.toWordList import toWordList

P = toWordList(answer='SimpleData.csv', question='DataQuestionExam_SMP.csv')
a, b, c, d = P.splitIO()

sentences = []
for a1 in a.loc[:,['Answer']].values:
	sentences.append(P.sentenceToWordList(a1[-1]))
print((sentences))