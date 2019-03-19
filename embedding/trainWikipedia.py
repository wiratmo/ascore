import io
import os
import sys
sys.path.insert(0, os.getcwd())
from module.toWordList import toWordList
from datetime import timedelta
from module.changeNum2WordandFilter import changeNum2WordandFilter
import multiprocessing
import time
import gensim

start_time = time.time()

fileName = "idwiki.txt"
fileSource = "idwiki.bz2"

def streamingWiki():
	print('Streaming wiki...')
	id_wiki = gensim.corpora.WikiCorpus(fileSource)
	article_count = 0

	with io.open(fileName, 'w') as wiki_txt:
		for text in id_wiki.get_texts():

			article_count += 1

			text = changeNum2WordandFilter().detectCombine(text)
			wiki_txt.write(" ".join(map(str, text)) + '\n')

			if article_count % 10000 == 0:
				print('{} articles processed'.format(article_count))

		print('total: {} articles'.format(article_count))

	finish_time = time.time()
	print('Elapsed time for streaming wiki: {}'.format(timedelta(seconds=finish_time-start_time)))

def trainingModelGensim():
	start_time = time.time()
	print('Training Word2Vec Model...')
	sentences = gensim.models.word2vec.LineSentence(fileName)
	id_w2v = gensim.models.word2vec.Word2Vec(sentences, size=200, workers=multiprocessing.cpu_count()-1)
	id_w2v.save('idwiki_word2vec_200.model')
	finish_time = time.time()

	print('Finished. Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))

def main():
	
	# streamingWiki()
	trainingModelGensim()

if __name__ == '__main__':
	main()