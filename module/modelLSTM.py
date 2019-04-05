class modelLSTM(object):
	from keras.models import Sequential
	from keras.layers import LSTM, Dense, Dropout, Bidirectional

	"""
		Buat opsi pertama dulu. dengan inpuan LSTM berupa average wrd embedding dalam sentence.
	"""
	def getModel(self):
		model = self.Sequential()
		model.add(self.LSTM(200, dropout=0.4, recurrent_dropout=0.4, input_dim=200, return_sequences=True))
		model.add(self.LSTM(64, recurrent_dropout=0.4))
		model.add(self.Dropout(0.5))
		model.add(self.Dense(1, activation='relu'))
		model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
		model.summary()

		return model	