# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from sklearn.decomposition import PCA
from sklearn import datasets
import matplotlib.pyplot as plt


iris = datasets.load_iris()
x = iris.data
y = iris.target
pca = PCA(n_components=2)
reduce_X = pca.fit_transform(x)

red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []

for i in range(len(reduce_X)):
    if y[i] == 0:
        red_x.append(reduce_X[i][0])
        red_y.append(reduce_X[i][1])
    elif y[i] == 1:
        blue_x.append(reduce_X[i][0])
        blue_y.append(reduce_X[i][1])
    else:
        green_x.append(reduce_X[i][0])
        green_y.append(reduce_X[i][1])
        

plt.figure()
plt.scatter(red_x,red_y,c='r',marker='x')
plt.scatter(blue_x,blue_y,c='b', marker='D')
plt.scatter(green_x,green_y,c='g', marker='.')
plt.show()

