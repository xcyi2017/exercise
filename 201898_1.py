# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 15:44:04 2018

@author: xcy
"""

import numpy as np

class Perception:
    
    def __init__(self, eta=0.01, n_iter=20):
        self.eta = eta
        self.n_iter = n_iter
        
    
    def than(self, x):
            if x != 0:
                return x/abs(x)
            else:
                return 0
        
    def fit(self, X, y):
        
        self.w_ = np.zeros(X.shape[1]+1)
        self.err = []
        for _ in range(self.n_iter):
            err = 0
            for xi, yi in zip(X, y):
               z = xi.dot(self.w_[1:]) + self.w_[0]
               beta = self.than(z)
               update = self.eta*(yi - beta)
               self.w_[1:] += update*xi
               self.w_[0] = update
               err += int((yi - beta) != 0.0)
            self.err.append(err)
        print(self.err)
        return self
    
    
    def predict(self,xi):
        return xi.dot(self.w_[1:])+self.w_[0]
    
X = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
y = np.array([-1, 1, 1, -1])          
p  =Perception()
p.fit(X,y)
print(p.predict(X))
print(p.w_)
        
           
        