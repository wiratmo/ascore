class modelLSTM(object):
	from keras.models import Sequential, Model
	from keras.layers import LSTM, Dense, Dropout, Bidirectional, Input, concatenate

	"""
		Buat opsi pertama dulu. dengan inpuan LSTM berupa average wrd embedding dalam sentence.
	"""
	def getModel(self):
		model = self.Sequential()
		model.add(self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, input_dim=200, return_sequences=True))
		model.add(self.LSTM(64, recurrent_dropout=0.5))
		model.add(self.Dropout(0.5))
		model.add(self.Dense(units=1, activation='relu'))
		model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
		model.summary()

		return model	

	def biGetModel(self, inputD):
		model = self.Sequential()
		model.add(self.Bidirectional(self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, return_sequences=True), input_shape=inputD))
		model.add(self.LSTM(64, recurrent_dropout=0.5))
		model.add(self.Dropout(0.5))
		x = model.add(self.Dense(units=30, activation='relu'))
		model.add(self.Dense(units=1, activation='relu'))
		model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
		model.summary()

		return x, model	

	def siamenseModel(self, inputD):

		print(inputD)
		MA = self.Input(shape=inputD,name='mai')
		MB = self.Input(shape=inputD,name='mbi')

		model = self.Model(inputs=[MA, MB], outputs=out)

		x = (self.Bidirectional(self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, return_sequences=True), input_shape=inputD))(MA)
		x = (self.LSTM(64, recurrent_dropout=0.5))(x)
		x = (self.Dropout(0.5))(x)
		x = (self.Dense(units=30, activation='relu'))(x)

		y = (self.Bidirectional(self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, return_sequences=True), input_shape=inputD))(MB)
		y = (self.LSTM(64, recurrent_dropout=0.5))(y)
		y = (self.Dropout(0.5))(y)
		y = (self.Dense(units=30, activation='relu'))(y)

		x = self.concatenate([x, y])

		out = self.Dense(1, activation='sigmoid')(x)


		model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])

		model.summary()

		return model	