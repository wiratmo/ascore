import io
import sys
sys.path.insert(0, '/home/safire/OneDrive/Kuliah/Tesis/')
from module.toWordList import toWordList
import multiprocessing
from module.changeNum2WordandFilter import changeNum2WordandFilter
import time
from datetime import timedelta
import gensim

start_time = time.time()

fileName = "enwiki.txt"
# print('Streaming wiki...')
# id_wiki = gensim.corpora.WikiCorpus('enwiki.bz2')
# article_count = 0

# with io.open(fileName, 'w') as wiki_txt:
# 	for text in id_wiki.get_texts():

# 		article_count += 1

# 		text = changeNum2WordandFilter().detectCombine(text)
# 		wiki_txt.write(" ".join(map(str, text)) + '\n')

# 		if article_count % 10000 == 0:
# 			print('{} articles processed'.format(article_count))

# 	print('total: {} articles'.format(article_count))

# finish_time = time.time()
# print('Elapsed time for streaming wiki: {}'.format(timedelta(seconds=finish_time-start_time)))

start_time = time.time()
print('Training Word2Vec Model...')
sentences = gensim.models.word2vec.LineSentence(fileName)
id_w2v = gensim.models.word2vec.Word2Vec(sentences, size=200, workers=multiprocessing.cpu_count()-1)
id_w2v.save('idwiki_word2vec_200.model')
finish_time = time.time()

print('Finished. Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))