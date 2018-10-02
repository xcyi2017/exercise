# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 09:45:09 2018

@author: xcy
"""

import os
import shutil


for name in os.listdir(r'C:/Users/xcy/Desktop/'):
    f = name.split('.')[-1]
    path = 'C:/Users/xcy/Desktop/' + f
    try:
        if not os.path.exists(path):
            os.makedirs(path)
            shutil.move('C:/Users/xcy/Desktop/'+name,path)
        else:
            shutil.move('C:/Users/xcy/Desktop/'+name,path)
    except:
        pass
