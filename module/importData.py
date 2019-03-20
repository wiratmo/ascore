class importData(object):

	import pandas as pd

	def __init__(self, answer, question):
		super(importData, self).__init__()
		self.answer = answer
		self.question = question
	
	def openData(self):
		dAnswer = self.pd.read_csv(self.answer).drop(columns=['Nama_Peserta']).sort_values(by=['Essay_id'])
		dQuestion = self.pd.read_csv(self.question)
		return dAnswer, dQuestion