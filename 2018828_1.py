# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 14:38:17 2018

@author: xcy
"""
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=3)

raw_data_X = np.array([
              [3.393533211, 2.331273381],
              [3.110073483, 1.781539638],
              [1.343808831, 3.368360954],
              [3.582294042, 4.679179110],
              [2.280362439, 2.866990263],
              [7.423436942, 4.696522875],
              [5.745051997, 3.533989803],
              [9.172168622, 2.511101045],
              [7.792783481, 3.424088941],
              [7.939820817, 0.791637231]
              ])

raw_data_y = np.array([0,0,0,0,0,1,1,1,1,1])

plt.scatter(raw_data_X[raw_data_y==0,0],raw_data_X[raw_data_y==0,1],marker='o')

plt.scatter(raw_data_X[raw_data_y==1,0],raw_data_X[raw_data_y==1,1],marker='^')

X = np.array([8,6])

def distance(X):
   return np.sqrt( ((X-raw_data_X)**2).sum(axis=1) )

dis_y = [(x1,x2) for x1, x2 in zip(distance(X), raw_data_y)]

dis_y_n = sorted(dis_y, key=lambda x:x[0])
print(dis_y_n)

n = 0
for i in dis_y_n[:3]:
    if i[1] == 0:
        n += 1
        
if n > 1:
    print('0')
else:
    print('1')
knn.fit(raw_data_X, raw_data_y)
print(knn.predict(X))

plt.scatter(X[0],X[1],marker='o' if n > 1 else '^')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
