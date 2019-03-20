class toVectore(object):

	import numpy as np
	
	def __init__(self, essays, model, numFeature):
		super(toVectore, self).__init__()
		self.essays = essays
		self.model = model
		self.numFeature = numFeature

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

	def changeToVector(self):
		counter = 0
		wordVectore = self.np.zeros((len(self.essays),self.numFeature),dtype="float32")
		for essay in self.essays:
			wordVectore[counter] = self.makeFeatureVec(essay)
			counter = counter + 1
		return wordVectore
		