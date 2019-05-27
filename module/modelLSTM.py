class modelLSTM(object):
	from keras.models import Sequential, Model
	from keras.layers import LSTM, Dense, Dropout, Bidirectional, Lambda, Dot
	import keras.backend as K
	from keras import optimizers

	def getModel(self):
		model = self.Sequential()
		model.add(self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, input_dim=200, return_sequences=True))
		model.add(self.LSTM(64, recurrent_dropout=0.5))
		model.add(self.Dense(units=64, activation='relu'))
		model.add(self.Dropout(0.5))
		model.add(self.Dense(units=1, activation='relu'))
		model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
		model.summary()
		return model	

	def biGetModel(self, inputD):
		model = self.Sequential()
		model.add(self.Bidirectional(self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, return_sequences=True), input_shape=inputD))
		model.add(self.LSTM(64, recurrent_dropout=0.5))
		model.add(self.Dense(units=64, activation='relu'))
		model.add(self.Dropout(0.5))
		model.add(self.Dense(units=1, activation='relu'))
		model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])
		model.summary()
		return model

	def siamenseModel(self, inputD):

		from keras.layers import Input, concatenate, subtract
		from keras import backend as K

		def euclidean_distance(vects):
			x, y = vects
			sum_square = K.sum(K.square(x - y), axis=1, keepdims=True)
			return K.sqrt(K.maximum(sum_square, K.epsilon()))

		def manhattan_distance(vects):
			x, y = vects
			return K.sum(K.abs(x - y), axis=1, keepdims=True)


		MA = Input(shape= inputD, dtype="float32")
		MB = Input(shape= inputD, dtype="float32")

		x = self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, return_sequences=True)(MA)
		x = self.LSTM(64, recurrent_dropout=0.5)(x)
		x = self.Dense(units=64, activation='relu')(x)

		y = self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, return_sequences=True)(MB)
		y = self.LSTM(64, recurrent_dropout=0.5)(y)
		y = self.Dense(units=64, activation='relu')(y)

		x = self.Dropout(0.5)(x)
		y = self.Dropout(0.5)(y)

		out = self.Lambda(function=lambda a: euclidean_distance(a),output_shape=lambda a: (a, 1))([x,y])

		out = self.Dense(1, activation='relu')(out)

		model = self.Model(inputs=[MA, MB], outputs=out)

		model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mae'])

		model.summary()

		return model	

	def biSiamenseModel(self, inputD, euclidean=False):

		from keras.layers import Input, concatenate, subtract, dot
		from keras import backend as K

		def euclidean_distance(vects):
			x, y = vects
			sum_square = K.sum(K.square(x - y), axis=1, keepdims=True)
			return K.sqrt(K.maximum(sum_square, K.epsilon()))

		def manhattan_distance(vects):
			x, y = vects
			return K.sum((K.abs(x - y)), axis=1, keepdims=True)

		def exponent_neg_manhattan_distance(vects):
			x, y = vects
			return K.exp(-K.sum(K.abs(x-y), axis=1, keepdims=True))


		MA = Input(shape= inputD, dtype="float32")
		MB = Input(shape= inputD, dtype="float32")

		x = self.Bidirectional(self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, return_sequences=False), input_shape=inputD)(MA)
		x = self.Dense(units=64, activation='sigmoid')(x)

		y = self.Bidirectional(self.LSTM(200, dropout=0.5, recurrent_dropout=0.5, return_sequences=False), input_shape=inputD)(MB)
		y = self.Dense(units=64, activation='sigmoid')(y)

		x = self.Dropout(0.5)(x)
		y = self.Dropout(0.5)(y)
		
		# a2 = (self.Lambda(function=lambda a: euclidean_distance(a),output_shape=lambda a: (a,1)))([x,y])

		if euclidean:
			a2 = (self.Lambda(function=lambda a: euclidean_distance(a),output_shape=lambda a: (a,1)))([x,y])
		else:
			a2 = concatenate([x,y])
		
		out = self.Dense(1, activation='relu')(a2)

		model = self.Model(inputs=[MA, MB], outputs=out)
		sgd = self.optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
		model.compile(loss='mean_squared_error', optimizer=sgd, metrics=['mae'])

		model.summary()

		return model	