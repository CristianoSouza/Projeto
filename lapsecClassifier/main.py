import numpy as np
from rnaModule import RnaModule
from knnModule import KnnModule
from dataSet import DataSet

dts = DataSet("base_iris.csv", "base_iris_teste.csv")
dts.load_data()

print("load data")
print(dts.get_data_set())
print(dts.get_test_data_set())

rna = RnaModule(dts.get_data_set(), dts.get_test_data_set())

knn = KnnModule(dts.get_data_set(), dts.get_test_data_set())


