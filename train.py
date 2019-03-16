class ascore(object):

	# import package
	import pandas as pd
	import numpy as np
	import nltk
	import re
	from nltk.corpus import stopwords
	from gensim.models import Word2Vec
	
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
		word = self.re.sub("[^a-zA-Z]", "", sentences)
		number = self.re.sub("[^1-9]", "", sentences)
		char = self.re.sub("[^a-zA-Z]", "", sentences) # character re untuk caracter blm tahu

		if : # equal antar senternce dengan word DENGAN OPREATOR OR; jika hasilnya true maka diulangi lagi, kalau false baru keluar senterncenya
			# dideteksi mana kata pertama; kalau kata pertama ditemukan simpan dulu ke variabel 
			pass
		else:
			pass

	def essayToWordList(self, sentences):
		sentences = self.re.split("\s", sentences)
		words = [self.mergedWord(w) for w in sentences]
		return (words)

P = ascore(answer='DataAnswerExam_SMP.csv', question='DataQuestionExam_SMP.csv')
a, b, c, d = P.splitIO()
sentences = []
for a1 in a.loc[:,['Answer']].values:
	sentences.append(P.essayToWordList(a1[-1]))
print(sentences[350])
print(a.iloc[350].values)