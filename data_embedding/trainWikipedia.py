import io
import sys
sys.path.insert(0, '/home/safire/OneDrive/Kuliah/Tesis/')
from module.toWordList import toWordList
from module.changeNum2WordandFilter import changeNum2WordandFilter
import time
from datetime import timedelta
import gensim


start_time = time.time()
print('Streaming wiki...')
id_wiki = gensim.corpora.WikiCorpus('enwiki.bz2')
article_count = 0

with io.open('enwiki.txt', 'w') as wiki_txt:
	for text in id_wiki.get_texts():

		article_count += 1

		text = changeNum2WordandFilter().detectCombine(text)
		wiki_txt.write(" ".join(map(str, text)) + '\n')

		if article_count % 10000 == 0:
			print('{} articles processed'.format(article_count))

	print('total: {} articles'.format(article_count))

finish_time = time.time()
print('Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))