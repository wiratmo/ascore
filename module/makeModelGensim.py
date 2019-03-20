class makeModelGensim(object):	
	
	import io
	import os
	import sys
	cwd = os.getcwd()
	sys.path.insert(0, cwd)
	from datetime import timedelta
	from module.changeNum2WordandFilter import changeNum2WordandFilter
	import multiprocessing
	import time
	import gensim

	dirData = cwd+'/data/'
	
	def __init__(self, wikiOutput, modelOutput, numDimension, trainingAlgoritm):
		super(makeModelGensim, self).__init__()
		self.wikiOutput = self.dirData+wikiOutput
		self.modelOutput = self.dirData+modelOutput
		self.numDimension = numDimension
		self.trainingAlgoritm = trainingAlgoritm

	def execute(self):
		start_time = self.time.time()
		print('Training Word2Vec Model...')
		sentences = self.gensim.models.word2vec.LineSentence(self.wikiOutput)
		id_w2v = self.gensim.models.word2vec.Word2Vec(sentences, size=self.numDimension, workers=self.multiprocessing.cpu_count()-1, sg=self.trainingAlgoritm)
		
		# id_w2v.save(self.modelOutput) 
		id_w2v.vw.save_word2vec_format(self.modelOutput)
		finish_time = self.time.time()

		print('Finished. Elapsed time: {}'.format(self.timedelta(seconds=finish_time-start_time)))