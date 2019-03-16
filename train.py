class ascore(object):

	# import package
	import pandas as pd
	import numpy as np
	import string
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

	def separateWords(self, words):
		# locWord = ''

		for word in words:
			
			mergedWord = list()

			alphabet = self.re.sub("[^a-zA-Z]", " ", word).replace(' ','')
			number = self.re.sub("[^0-9]", " ", word).replace(' ','')
			symbol = self.re.sub('[^/%/*()\-=+.,><":]', " ", word).replace(' ','')
			

			# y = A'B'C + A'BC' + AB'C'
			if (((not(not alphabet)) and (not(not number)) and (not symbol)) or ((not(not alphabet)) and (not number) and (not(not symbol))) or ((not alphabet) and (not(not number)) and (not(not symbol)))):
				print(word)
				locWord = words.index(word)
				dtype = [('loc', int), ('value', 'U20')]
				
				# looping terus karena word e sing pertama nda iso ganti.
				if not(not alphabet):
					mergedWord.append((word.index(alphabet), alphabet))
				if not(not number):
					mergedWord.append((word.index(number), number))
				if not(not symbol):
					mergedWord.append((word.index(symbol), symbol))

				mergedWord = self.np.array(mergedWord, dtype=dtype)
				mergedWord = self.np.sort(mergedWord, order='loc')

				a = locWord
					
				for mw in mergedWord:
					if a == locWord:
						words[a] = mw[1]
						a += 1
					else:
						words.insert(a, mw[1])

		return words

	def sentenceToWordList(self, sentences):

		essay_v = self.re.sub("[^a-zA-Z0-9/%/*\-=+.,><':]", " ", sentences)
		words = essay_v.split()
		return self.separateWords(words)


P = ascore(answer='SimpleData.csv', question='DataQuestionExam_SMP.csv')
a, b, c, d = P.splitIO()

sentences = []
for a1 in a.loc[:,['Answer']].values:
	sentences.append(P.sentenceToWordList(a1[-1]))
print((sentences))

# no3 = (c.loc[:,['Answer']].values)[2]
# print(P.sentenceToWordList(no3[-1]))
