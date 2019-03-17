import io
import time
from datetime import timedelta

import gensim

start_time = time.time()
print('Streaming wiki...')
id_wiki = gensim.corpora.WikiCorpus('enwiki-latest-pages-articles-multistream-index3.txt-p88445p200507.bz2', lemmatize=False, dictionary={})
article_count = 0
print(id_wiki.get_texts())
with io.open('idwiki.txt', 'w') as wiki_txt:
	for text in id_wiki.get_texts():
		print(text)
		wiki_txt.write(" ".join(map(unicode, text)) + '\n')
		article_count += 1

		if article_count % 10000 == 0:
			print('{} articles processed'.format(article_count))

	print('total: {} articles'.format(article_count))

finish_time = time.time()
print('Elapsed time: {}'.format(timedelta(seconds=finish_time-start_time)))