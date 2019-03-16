class ascore(object):

	# import package
	import pandas as pd
	import numpy as np
	import re
	from gensim.models import Word2Vec

	gWord = []
	
	def __init__(self, answer, question):
		super(ascore, self).__init__()
		self.answer = answer
		self.question = question

	def openData(self):
		dAnswer = self.pd.read_csv(self.answer).drop(columns=['Nama_Peserta']).sort_values(by=['Essay_id'])
		dQuestion = self.pd.read_csv(self.question)
		return dAnswer, dQuestion

	def splitIO(self):
		dAnswer, dQuestion = self.openData()
		xAnswer = dAnswer.loc[:, ['Essay_id', 'Answer']]
		xQuestion = dQuestion.loc[:, ['Question']]
		xTAnswer = dQuestion.loc[:, ['Answer']]
		yScore = dAnswer.loc[:, ['Score']]
		return xAnswer, xQuestion, xTAnswer, yScore

	def mergedWord(self, sentences):
		word = self.re.sub("[^a-zA-Z]", " ", sentences).replace(' ','')
		number = self.re.sub("[^0-9]", " ", sentences).replace(' ','')
		char = self.re.sub('[^/%/*()\-=+.,><":]', " ", sentences).replace(' ','')

		print("--------")
		print("ini word ..."+word)
		print("ini number ..."+number)
		print("ini char ..."+char)

		if ((word == sentences) or (number == sentences) or (char == sentences)):
			if len(self.gWord)>0:
				self.gWord.append(sentences)
				print(self.gWord)
				return self.gWord
			return sentences
		else:
			# check dulu ada ga nya, kaau ada baru dibandingkan
			
			w = sentences.find(word)
			n = sentences.find(number)
			c = sentences.find(char)
			print(w)
			print(n)
			print(c)
			if ((w < c) and (w <n)):
				self.gWord.append(w)
				sentences = sentences.replace(w, '')
				return mergedWord()
			elif ((n < c) and (n < w)) :
				self.gWord.append(c)
				sentences = sentences.replace(n, '')
				return mergedWord()
			elif ((c < w) and (c <n)) :
				self.gWord.append(c)
				sentences = sentences.replace(c, '')
				return mergedWord()
		pass

	def essayToWordList(self, sentences):
		sentences = self.re.split("\s", sentences)
		words = [self.mergedWord(w) for w in sentences]
		return (words)


P = ascore(answer='DataAnswerExam_SMP.csv', question='DataQuestionExam_SMP.csv')
a, b, c, d = P.splitIO()

#  disable sementara untuk mempersingkat waktu

# sentences = []
# for a1 in c.loc[:,['Answer']].values:
# 	sentences.append(P.essayToWordList(a1[-1]))
# print(sentences[2])

no3 = (c.loc[:, ['Answer']].values)[2]
print(no3)
print(P.essayToWordList(no3[-1]))
