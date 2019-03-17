from module.toWordList import toWordList
from num2words import num2words

P = toWordList(answer='DataAnswerExam_SMP.csv', question='DataQuestionExam_SMP.csv')
a, b, c, d = P.splitIO()

# sentences = []
# for a1 in c.loc[:,['Answer']].values:
# 	sentences.append(P.sentenceToWordList(a1[-1]))
# print((sentences))

print(P.sentenceToWordList((c.loc[:,['Answer']].values)[2][-1]))

print(num2words(240, lang='id'))