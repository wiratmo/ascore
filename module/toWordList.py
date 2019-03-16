class toWordList(object):

	# import package
	import pandas as pd
	import numpy as np
	import string
	import re
	from gensim.models import Word2Vec

	def __init__(self, answer, question):
		super(toWordList, self).__init__()
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

		for word in words:
			
			mergedWord = list()

			alphabet = (self.re.sub("[^a-zA-Z]", " ", word)).split()
			number = (self.re.sub("[^0-9]", " ", word)).split()
			symbol = (self.re.sub('[^/%/*()\-=+.,><":]', " ", word)).split()


			# y = A'B'C + A'BC' + AB'C'
			if (((not(not alphabet)) and (not(not number)) and (not symbol)) or ((not(not alphabet)) and (not number) and (not(not symbol))) or ((not alphabet) and (not(not number)) and (not(not symbol)))):

				locWord = words.index(word)
				dtype = [('loc', int), ('value', 'U20')]

				[mergedWord.append((word.index(alpa), alpa)) for alpa in alphabet if not(not(alphabet))]
				[mergedWord.append((word.index(num), num)) for num in number if not(not(number))]
				[mergedWord.append((word.index(sym), sym)) for sym in symbol if not(not(symbol))]


				mergedWord = self.np.array(mergedWord, dtype=dtype)
				mergedWord = self.np.sort(mergedWord, order='loc')

				a = locWord
					
				for mw in mergedWord:

					if a == locWord:
						words[a] = mw[1]
					else:
						words.insert(a, mw[1])
	
					a += 1

		return words

	def sentenceToWordList(self, sentences):

		essay_v = self.re.sub("[^a-zA-Z0-9/%/*\-=+.,><'():]", " ", sentences)
		words = essay_v.split()
		return self.separateWords(words)
