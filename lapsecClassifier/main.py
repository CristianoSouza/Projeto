import numpy as np
from rnaModule import RnaModule
from knnModule import KnnModule
from dataSet import DataSet

dts = DataSet("base_iris.csv")
dts.load_data()

print("load data")

for i_fold in range(0,10):

	sub_data_set = dts.load_sub_data_set("sub_data_set_" + str(i_fold+1 ) + ".csv")
	print(sub_data_set[:,1:])

	#rna = RnaModule(dts.get_data_set(), sub)

	#knn = KnnModule(dts.get_data_set(), dts.get_test_data_set())


