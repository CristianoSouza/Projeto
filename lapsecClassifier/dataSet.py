import pandas


class DataSet(object):

	file_name = ""
	test_file_name = ""
	data_set = []
	test_data_set = []

	def __init__(self, file_name, test_file_name):
		self.file_name = file_name
		self.test_file_name = test_file_name

	def load_data(self):
		dataframe = pandas.read_csv("bases/" + self.file_name)
		self.data_set = dataframe.values

		test_dataframe = pandas.read_csv("bases/" + self.test_file_name)
		self.test_data_set = test_dataframe.values

	def get_data_set(self):
		return self.data_set

	def get_test_data_set(self):
		return self.test_data_set
 