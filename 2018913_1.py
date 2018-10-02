# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 08:35:15 2018

@author: xcy
"""

import numpy as np

X = np.array([
             [0, 0, 1], 
             [1, 1, 1], 
             [1, 0, 1], 
             [0, 1, 1]])
X = [x.reshape(-1,1) for x in X]

y = np.array([0, 1, 1, 0]) 
eta = 0.001
w = np.random.randn(1,3)
b = np.random.randn(1,1)


for _ in range(100000):
    nabla_w = np.random.randn(1,3)
    nabla_b = np.random.randn(1,1)
    for xi, yi in zip(X, y):
        z = np.dot(w, xi)+b
        a = 1/(1+np.exp(-z))
        delta = (a - yi)*a*(1-a)
        delta_b = delta
        delta_w = np.dot(delta, xi.transpose())
        nabla_w += delta_w
        nabla_b += delta_b
    w -= eta*nabla_w*len(X)
    b -= eta*nabla_b*len(X)
    

for x in X:
    res = np.dot(w,x)+b
    print(1/(1+np.exp(-res)))
    
        