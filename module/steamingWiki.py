class steamingWiki(object):
	import io
	import os
	import sys
	cwd = os.getcwd()
	sys.path.insert(0, cwd)
	from datetime import timedelta
	from module.changeNum2WordandFilter import changeNum2WordandFilter
	import time
	import gensim

	dirData = cwd+'/data/'
	
	def __init__(self, corpusInput, wikiOutput):
		super(steamingWiki, self).__init__()
		self.corpusInput = self.dirData+corpusInput
		self.wikiOutput = self.dirData+wikiOutput
	
	def execute(self):
		start_time = self.time.time()
		print('Streaming wiki...')
		id_wiki = self.gensim.corpora.WikiCorpus(self.corpusInput)
		article_count = 0

		with self.io.open(self.wikiOutput, 'w') as wiki_txt:
			for text in id_wiki.get_texts():

				article_count += 1

				text = self.changeNum2WordandFilter().detectCombine(text)
				wiki_txt.write(" ".join(map(str, text)) + '\n')

				if article_count % 10000 == 0:
					print('{} articles processed'.format(article_count))

			print('total: {} articles'.format(article_count))

		finish_time = self.time.time()
		print('Elapsed time for streaming wiki: {}'.format(self.timedelta(seconds=finish_time-start_time)))