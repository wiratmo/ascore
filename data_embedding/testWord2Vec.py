import sys
sys.path.insert(0, '/home/safire/OneDrive/Kuliah/Tesis/')
from module.toWordList import toWordList
from gensim.models import Word2Vec

P = toWordList(answer='DataAnswerExam_SMP.csv', question='DataQuestionExam_SMP.csv')
xAnswer, xQuestion, xTAnswer, yScore = P.splitIO()

sentences = []

for a1 in xAnswer.loc[:,['Answer']].values:
	sentences.append(P.sentenceToWordList(a1[-1]))

for a1 in xTAnswer.loc[:,['Answer']].values:
	sentences.append(P.sentenceToWordList(a1[-1]))


print(sentences)

model = Word2Vec(sentences, min_count=1)

# summarize the loaded model
print(type(model))
# summarize vocabulary
words = list(model.wv.vocab)
print(words)
# access vector for one word
print(model['240'])
# save model
model.save('model.bin')
# load model
new_model = Word2Vec.load('model.bin')
print(new_model)