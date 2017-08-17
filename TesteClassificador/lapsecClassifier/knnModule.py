import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas 
from sklearn import neighbors

class KnnModule(object):
	data_set_samples = []
	data_set_labels = []
	test_data_set_samples = []
	test_data_set_labels = []

	def __init__(self, data_set, test_data_set):
		print((len(data_set[1])-1))
		self.data_set_samples = data_set[:,0:(len(data_set[0])-1)]
		self.data_set_labels = data_set[:,(len(data_set[0])-1)]
		self.test_data_set_samples = test_data_set[:,0:(len(test_data_set[0])-1)]
		self.test_data_set_labels = test_data_set[:,(len(test_data_set[0])-1)]

		print(self.data_set_samples)
		print(self.data_set_labels)
		print(self.test_data_set_samples)
		print(self.test_data_set_labels)
