class changeNum2WordandFilter(object):

	import re

	def detectCombine(self, texts):

		from num2words import num2words

		altText = list(texts)

		for text in texts:
			alphabet = (self.re.sub("[^a-zA-Z]", " ", text)).split()
			number = (self.re.sub("[^0-9]", " ", text)).split()
			symbol = (self.re.sub('[^/%/*()\-=+.,><":]', " ", text)).split()



			# y = A'B'C + A'BC' + AB'C'
			if (((not(not alphabet)) and (not(not number)) and (not symbol)) or ((not(not alphabet)) and (not number) and (not(not symbol))) or ((not alphabet) and (not(not number)) and (not(not symbol)))):
				altText.remove(text)
			else:
				if not(not(number)):

					locWord = altText.index(text)

					num = int(number[-1])
					toSingleWord = (str(num2words(num, lang='en'))).split()

					a = locWord

					for tsw in toSingleWord:

						if a == locWord:
							altText[a] = tsw
						else:
							altText.insert(a, tsw)
						a += 1
		return altText