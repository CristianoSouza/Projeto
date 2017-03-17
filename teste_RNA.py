'''Trains a simple deep NN on the MNIST dataset.
Gets to 98.40% test accuracy after 20 epochs
(there is *a lot* of margin for parameter tuning).
2 seconds per epoch on a K520 GPU.
'''

from __future__ import print_function
import numpy as np
import os.path
import pandas 
from keras.datasets import mnist
from keras.callbacks import CSVLogger
from keras.wrappers.scikit_learn import KerasClassifier
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.optimizers import RMSprop
from keras.utils import np_utils
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold



dataframe = pandas.read_csv("bases/base_iris.csv")
base_dados = dataframe.values
 
dataframe_teste = pandas.read_csv("bases/base_iris_teste.csv")
base_dados_teste = dataframe_teste.values


seed = 7

X = base_dados[:,0:4]
Y = base_dados[:,4]
print(X)
print("----")
print(Y)
print("--------------------------------")
X_teste = base_dados_teste[:,0:4]
Y_teste = base_dados_teste[:,4]
print(X_teste)
print("----")
print(Y_teste)

# encode class values as integers
encoder = LabelEncoder()
encoder.fit(Y)
encoded_Y = encoder.transform(Y)
# convert integers to dummy variables (i.e. one hot encoded)
dummy_y = np_utils.to_categorical(encoded_Y)


model = Sequential()
model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
model.add(Dense(4, input_dim=4, init='normal', activation='relu'))
model.add(Dense(1, init='normal', activation='tanh'))
	# Compile model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

print(model.output_shape)
csv_logger = CSVLogger('training.log')
a = model.fit(X, Y, nb_epoch=150, batch_size=10, callbacks=[csv_logger])
print(a)


# calculate predictions
predictions = model.predict_classes(X_teste)
print(predictions)
# round predictions 
#rounded = [round(x[0]) for x in predictions]
#print(rounded)

'''# evaluate the model
scores = model.evaluate(X_teste, Y_teste)
print("asdasd")
print(" %s : %.2f%%- " % (model.metrics_names[1], scores[1]*100))
'''
dados = { 'posicao_base': [34, 78], 'a': [5.0, 5], 'b': [3.5, 5], 'c':[1.3, 5], 'd': [0.3, 5], 'classe': [0,1]}
teste = pandas.DataFrame(dados, columns = ['posicao_base','a','b','c','d','classe'])
teste.to_csv("out.csv", index=False, sep=',')

dataframe_out = pandas.read_csv("out.csv")
print(dataframe_out)
base_out = dataframe_out.values
print(base_out)

posicao_base = base_out[:,0]
X = base_out[:,1:5]
Y = base_out[:,5]

print(posicao_base)
print(X)
print(Y)
