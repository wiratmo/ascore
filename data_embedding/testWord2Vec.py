import sys
sys.path.insert(0, '/home/safire/OneDrive/Kuliah/Tesis/')
from module.importData import importData
from module.toWordList import toWordList
from gensim.models import Word2Vec

xAnswer, xQuestion, xTAnswer, yScore = importData(answer='DataAnswerExam_SMP.csv', question='DataQuestionExam_SMP.csv').ExposeData()

sentences = []

for a1 in xAnswer.loc[:,['Answer']].values:
	sentences.append(toWordList().sentenceToWordList(a1[-1], changeNumber2Word= True))

for a1 in xTAnswer.loc[:,['Answer']].values:
	sentences.append(toWordList().sentenceToWordList(a1[-1], changeNumber2Word= True))

print(sentences)

model = Word2Vec(sentences, min_count=1)

# summarize the loaded model
print((model))
# summarize vocabulary
words = list(model.wv.vocab)
print(words)
# access vector for one word
print(model['dua'])
# save model
model.save('model.bin')
# load model
new_model = Word2Vec.load('model.bin')
print(new_model)