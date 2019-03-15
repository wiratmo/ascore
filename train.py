class ascore(object):

	# import package
	import pandas as pd
	import numpy as np
	import nltk
	nltk.download('stopwords')
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

	def essayToWordList(self, sentences, remove_stopwords = True):
		sentences = self.re.sub("[^a-zA-Z0-9/]"," ", sentences)
		words = sentences.lower().split()
		if remove_stopwords:
			stops = set(P.stopwords.words("indonesian"))
			words = [w for w in words if not w in stops]
		return (words)

P = ascore(answer='DataAnswerExam_SMP.csv', question='DataQuestionExam_SMP.csv')
a, b, c, d = P.splitIO()
sentences = []
for a1 in a.loc[:,['Answer']].values:
	sentences.append(P.essayToWordList(a1[0]))
print(len(sentences))
print(sentences[350])
