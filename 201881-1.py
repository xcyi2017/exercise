# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 11:29:02 2018

@author: xcy
"""

from sklearn.svm import SVC
import matplotlib.pyplot as plt
import numpy as np
from sklearn.learning_curve import validation_curve
from sklearn.datasets import load_digits

digits = load_digits()
X = digits.data
y = digits.target
param_range = np.logspace(-6,-2.3,5)

train_loss, test_loss = validation_curve(SVC(), X, y, param_name = 'gamma', cv = 5,param_range = param_range, scoring = 'mean_squared_error')
trian_loss_mean = -np.mean(train_loss,axis=1)
test_loss_mean = -np.mean(test_loss, axis=1)

plt.plot(param_range, trian_loss_mean, 'o-',color='r',label='Training')
plt.plot(param_range, test_loss_mean,'o-',color='g',label='Cross_validation')
plt.xlabel('Training examples')
plt.ylabel('Loss')
plt.legend()

plt.show()