import os

file_path = "my/directory/filename.txt"

directory = os.path.dirname(file_path)
if not os.path.exists(directory):
	print("nao existe")
	os.makedirs(directory)
else:
	print("exists")	