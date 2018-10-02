# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 10:57:06 2018

@author: xcy
"""

import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import numpy as np
import time


x = np.random.rand(100,2)
y=0.2*x[:,0]+x[:,1]*0.1 +1

t0 = time.time()
F1 = lm.RidgeCV()

F1.fit(x,y)
y1 = F1.predict(x)
t1 =time.time()

plt.plot(x,y,'go',x,y1,'r.')