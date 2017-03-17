import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas 
from sklearn import neighbors


dataframe = pandas.read_csv("bases/base_iris.csv")
base_dados = dataframe.values
 
dataframe_teste = pandas.read_csv("bases/base_iris_teste.csv")
base_dados_teste = dataframe_teste.values


n_neighbors = 1

X = base_dados[:,0:4]
y = base_dados[:,4]
print(X)
print("----")
print(y)
print("--------------------------------")
X_teste = base_dados_teste[:,0:4]
Y_teste = base_dados_teste[:,4]
print(X_teste)
print("----")
print(Y_teste)

h = .02 

# Create color maps
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # we create an instance of Neighbours Classifier and fit the data.
    clf = neighbors.KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)
    print(clf.predict(X_teste))
    print(clf.score(X_teste,Y_teste))

'''
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))

plt.show()
'''