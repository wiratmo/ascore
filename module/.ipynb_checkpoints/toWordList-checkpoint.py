class toWordList(object):

	import numpy as np
	import re
	
	def separateWords(self, words, changeNumber2Word=False):
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

		if changeNumber2Word:
			return self.changeNumber2Word(words)

		return words

	def changeNumber2Word(self, words):

		from num2words import num2words

		for word in words:
			number = (self.re.sub("[^0-9]", " ", word)).split()

			if not(not(number)):

				locWord = words.index(word)

				num = int(number[-1])
				toSingleWord = (str(num2words(num, lang='id'))).split()

				a = locWord

				for tsw in toSingleWord:

					if a == locWord:
						words[a] = tsw
					else:
						words.insert(a, tsw)
					a += 1

		return words

	def sentenceToWordList(self, sentences, changeNumber2Word = False):

		# essay_v = self.re.sub("[^a-zA-Z0-9/%/*\-=+.,><'():]", " ", sentences)
		essay_v = self.re.sub("[^a-zA-Z0-9]", " ", sentences)
		words = essay_v.split()
		print(words)
		return words
