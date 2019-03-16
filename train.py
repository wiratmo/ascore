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
		word = self.re.sub("[^a-zA-Z]", " ", sentences)
		# number = self.re.sub("[^1-9]", " ", sentences)
		char = self.re.sub('[^/%/*()\-=+.,><":]', " ", sentences) # character re untuk caracter blm tahu

		# if ((words == sentences) or (number == sentences) or (char == sentences)):
		if ((word == sentences)  or (char == sentences)):
			if len(self.gWord)>0:
				self.gWord.append(sentences)
				return self.gWord
			print(sentences)
			return sentences
		else:
			w = sentences.find(word)
			# n = sentences.find(number)
			c = sentences.find(char)
			if ((w < c)):
				self.gWord.append(w)
				sentences = sentences.replace(w, '')
				return mergedWord()
			elif c < w :
				self.gWord.append(c)
				sentences = sentences.replace(c, '')
				return mergedWord()
		pass

	def essayToWordList(self, sentences):
		sentences = self.re.split("\s", sentences)
		print(sentences)
		words = [self.mergedWord(w) for w in sentences]
		return (words)


P = ascore(answer='DataAnswerExam_SMP.csv', question='DataQuestionExam_SMP.csv')
a, b, c, d = P.splitIO()
sentences = []
for a1 in c.loc[:,['Answer']].values:
	sentences.append(P.essayToWordList(a1[-1]))
print(sentences[2])
print((c.loc[:, ['Answer']].values)[2])
