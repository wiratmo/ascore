class toVectore(object):
	"""
		Masih perlu diperluas dengan beberapa opsi.
	"""
	import numpy as np
	
	def __init__(self, essays, model, numFeature, average=True, trueAnswer=None):
		super(toVectore, self).__init__()
		self.essays = essays
		self.model = model
		self.numFeature = numFeature
		self.average = average
		self.trueAnswer = trueAnswer

	def makeFeatureVec(self, essay):
		sentenceVectore = self.np.zeros((self.numFeature,),dtype="float32")
		num_words = 0
		index2word_set = set(self.model.wv.index2word)
		for word in essay:
			if word in index2word_set:
				num_words += 1
				sentenceVectore = self.np.add(sentenceVectore, self.model[word])        
		sentenceVectore = self.np.divide(sentenceVectore,num_words)
		return sentenceVectore

	def changeToAverageVector(self):
		counter = 0
		wordVectore = self.np.zeros((len(self.essays),self.numFeature),dtype="float32")
		for essay in self.essays:
			wordVectore[counter] = self.makeFeatureVec(essay)
			counter = counter + 1
		wordVectore = self.np.reshape(wordVectore, (wordVectore.shape[0], 1, wordVectore.shape[1]))
		return wordVectore

	def makeSentenceVectore(self, essay, nEssay):
		sentenceVectore = self.np.zeros((nEssay, self.numFeature),dtype="float32")
		num_words = 0
		index2word_set = set(self.model.wv.index2word)
		for word in essay:
			if word in index2word_set:
				sentenceVectore[num_words] = self.model[word]
			num_words += 1
		# print("per sentence"+str(sentenceVectore.shape))
		return sentenceVectore

	def sentenceVectores(self):
		nEssay = []
		[(nEssay.append(len(essay))) for essay in self.essays]
		senteceVectore = self.np.zeros((len(self.essays), max(nEssay), self.numFeature), dtype="float32")
		
		# print("ini essay venctore kosong"+str(senteceVectore.shape))
		counter = 0
		for essay in self.essays:
			senteceVectore[counter] = self.makeSentenceVectore(essay, max(nEssay))
			counter += 1
		
		if self.trueAnswer is not None:
			trueAnswer = self.np.zeros((1, max(nEssay), self.numFeature), dtype="float32")
			countera = 0
			for ta in self.trueAnswer:
				trueAnswer[countera] = self.makeSentenceVectore(ta, max(nEssay))
				countera += 1

		# print("ini essay venctore isi"+str(senteceVectore.shape))
		self.np.reshape(senteceVectore, (senteceVectore.shape[1], senteceVectore.shape[0], senteceVectore.shape[2]))
		if self.trueAnswer is not None:
			self.np.reshape(trueAnswer, (trueAnswer.shape[1], trueAnswer.shape[0], trueAnswer.shape[2]))
			return senteceVectore, trueAnswer
		else:
			return senteceVectore

		

	def changeToVector(self):
		if self.average:
			return self.changeToAverageVector()
		else:
			return self.sentenceVectores()