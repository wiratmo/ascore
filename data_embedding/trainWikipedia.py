import io
import time
from datetime import timedelta

import gensim

import gensim

start_time = time.time()

id_wiki = gensim.corpora.WikiCorpus('enwiki.bz2')

for text in id_wiki.get_texts():
	print(text)

finish_time = time.time()
print('Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))