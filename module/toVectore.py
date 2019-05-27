class toVectore(object):
	"""
		Masih perlu diperluas dengan beberapa opsi.
	"""
	import numpy as np
	
	def __init__(self, essays, model, numFeature, average=True, trueAnswer=None, distance=False, question=None):
		super(toVectore, self).__init__()
		self.essays = essays
		self.model = model
		self.numFeature = numFeature
		self.average = average
		self.trueAnswer = trueAnswer
		self.distance = distance
		self.question = question

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
		trueAnswerVectore = self.np.zeros((len(self.essays),self.numFeature),dtype="float32")
		for essay in self.essays:
			wordVectore[counter] = self.makeFeatureVec(essay)
			counter = counter + 1
		if self.trueAnswer is not None:
			countera = 0
			for ta in self.trueAnswer:
				trueAnswerVectore[countera]  = self.makeFeatureVec(essay)
				countera = countera +1


		wordVectore = self.np.reshape(wordVectore, (wordVectore.shape[0], 1, wordVectore.shape[1]))
		trueAnswerVectore = self.np.reshape(trueAnswerVectore, (trueAnswerVectore.shape[0], 1, trueAnswerVectore.shape[1]))
		return wordVectore, trueAnswerVectore

	def makeSentenceVectore(self, essay, nEssay):
		sentenceVectore = self.np.zeros((nEssay, self.numFeature),dtype="float32")
		num_words = nEssay - len(essay)
		index2word_set = set(self.model.wv.index2word)
		for word in essay:
			if word in index2word_set:
				sentenceVectore[num_words] = self.model[word]
			num_words += 1
		
		return sentenceVectore

	def sentenceVectores(self):
		nEssay = 200

		senteceVectore = self.np.zeros((len(self.essays), nEssay, self.numFeature), dtype="float32")
		
		counter = 0
		for essay in self.essays:
			senteceVectore[counter] = self.makeSentenceVectore(essay, nEssay)
			counter += 1
		
		if self.trueAnswer is not None:
			trueAnswer = self.np.zeros((len(self.trueAnswer), nEssay, self.numFeature), dtype="float32")
			countera = 0
			for ta in self.trueAnswer:
				trueAnswer[countera] = self.makeSentenceVectore(ta, nEssay)
				countera += 1

		if self.trueAnswer is not None:
			if self.distance:
				distanceVectore = self.np.zeros((len(self.essays), nEssay, self.numFeature), dtype="float32")
				# ones = self.np.ones((len(self.essays), nEssay, self.numFeature), dtype="float32")
				for x in range(len(senteceVectore)):
					distanceVectore[x] = (senteceVectore[x] - trueAnswer[0])
				self.np.reshape(senteceVectore, (senteceVectore.shape[0], senteceVectore.shape[1], senteceVectore.shape[2]))
				self.np.reshape(distanceVectore, (distanceVectore.shape[0], distanceVectore.shape[1], distanceVectore.shape[2]))
				return senteceVectore, distanceVectore
			else :
				distanceVectore = self.np.zeros((len(self.essays), nEssay, self.numFeature), dtype="float32")
				# ones = self.np.ones((len(self.essays), nEssay, self.numFeature), dtype="float32")
				for x in range(len(senteceVectore)):
					distanceVectore[x] = trueAnswer[0]
				self.np.reshape(senteceVectore, (senteceVectore.shape[0], senteceVectore.shape[1], senteceVectore.shape[2]))
				self.np.reshape(distanceVectore, (distanceVectore.shape[0], distanceVectore.shape[1], distanceVectore.shape[2]))
				return senteceVectore, distanceVectore

			self.np.reshape(senteceVectore, (senteceVectore.shape[0], senteceVectore.shape[1], senteceVectore.shape[2]))
			self.np.reshape(trueAnswer, (trueAnswer.shape[0], trueAnswer.shape[1], trueAnswer.shape[2]))
			return senteceVectore, trueAnswer
		else:
			self.np.reshape(senteceVectore, (senteceVectore.shape[0], senteceVectore.shape[1], senteceVectore.shape[2]))
			return senteceVectore

		

	def changeToVector(self):
		if self.average:
			return self.changeToAverageVector()
		else:
			return self.sentenceVectores()