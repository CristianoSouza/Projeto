import pandas
import os
import random

class DataSet(object):

	file_name = ""
	test_file_name = ""
	dataframe_data_set = []
	partition_size = 0

	def __init__(self, file_name):
		self.file_name = file_name

	def load_data(self):
		self.dataframe_data_set = pandas.read_csv("bases/" + self.file_name)
		self.partition_data_set()

	def get_data_set(self):
		return self.data_set

	def select_examples(self):
		lista = range(0, self.dataframe_data_set.shape[0])
		data_set = []
		data_set_posicoes = []
		for i in range(0,10):
			sub_data_set = []
			posicoes = random.sample(lista,self.partition_size)
			print(posicoes)
			for j in range(0,len(posicoes)):
				lista.remove(posicoes[j])
				sub_data_set.append(self.dataframe_data_set.values[posicoes[j],:])
			data_set.append(sub_data_set)
			data_set_posicoes.append(posicoes)
			print('values:', data_set[i])
		print('posicoes:', data_set_posicoes)
		return data_set, data_set_posicoes

	def partition_data_set(self):
		print('Quatidade de exemplos:', self.dataframe_data_set.shape[0])
		self.partition_size = (self.dataframe_data_set.shape[0] / 10)
		print('10 Particoes de tamanho: ', self.partition_size)	

		examples, examples_posicoes = self.select_examples()
		for i in range(0,10):
			print('------------')	
			print('Particao ', i )
			sub_dataframe = pandas.DataFrame(
				data= examples[i],
				#index=range((i*self.partition_size),((i*self.partition_size) + self.partition_size) ), 
				index= examples_posicoes[i],
				columns= self.dataframe_data_set.columns )
			print(sub_dataframe)

			file_path = "bases/sub_bases/"

			directory = os.path.dirname(file_path)
			if not os.path.exists(directory):
				print("nao existe")
				os.makedirs(directory)
			else:
				print("exists")	

			sub_dataframe.to_csv("bases/sub_bases/sub_data_set_" + str(i+1) + ".csv", sep=',')

	def load_sub_data_set(self, file_name):
		sub_dataframe_data_set = pandas.read_csv("bases/sub_bases/" + file_name)
		return sub_dataframe_data_set.values


 