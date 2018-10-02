# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 13:20:45 2018

@author: xcy
"""

from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV

iris = load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state= 666)
param_grid =[
        {'weights':['uniform'],
         'n_neighbors':[i for i in range(1,11)]},
         {'weights':['distance'],
          'n_neighbors':[i for i in range(1,11)],
          'p':[i for i in range(1,6)]}
        ]

knn_clf = KNeighborsClassifier()
grid_seach = GridSearchCV(knn_clf, param_grid,n_jobs=1,verbose=2)
grid_seach.fit(X, y)
print(grid_seach.best_estimator_)
print(grid_seach.best_score_)
print(grid_seach.best_params_)