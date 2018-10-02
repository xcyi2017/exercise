# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:09:09 2018

@author: xcy
"""

from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

loaded_data = datasets.load_boston()
data_X = loaded_data.data
data_Y = loaded_data.target


linear = LinearRegression()
data_X_train, data_X_test, data_Y_train, data_y_test = train_test_split(data_X, data_Y, test_size=1/3, random_state=42)  

linear.fit(data_X_train,data_Y_train) 
score_ = linear.score(data_X_test,data_y_test)
predit_ = linear.predict(data_X_test[:4,:])    
print('得分是：{}\n实际值是：{}\n预测值是：{}'.format(score_,data_y_test[:4], predit_))
X, y = datasets.make_regression(n_samples=100, n_features=1,n_targets=1,noise=100)
plt.scatter(X,y)
plt.show()
