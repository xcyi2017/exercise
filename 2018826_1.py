# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 09:51:30 2018

@author: xcy
"""

import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
sex = {
       'M':0,
       'F':1,
       'I':2
       }
train_data = pd.read_csv('../DATA/traindata.csv')
test_data = pd.read_csv('../DATA/testdata.csv')
train_data['Sex']=train_data['Sex'].map(sex)
test_data['Sex'] = test_data['Sex'].map(sex)

x = train_data.iloc[:,range(len(train_data.columns)-1)]
y = train_data.Rings

KR = KNeighborsRegressor()
KR.fit(x,y)
Y = KR.predict(test_data)
test_data['Rings'] = Y
test_data.to_csv('../DATA/testdata1.csv')

#pca= PCA(n_components=4)
#Train = pca.fit_transform(train_data)
#Test = pca.transform(test_data)