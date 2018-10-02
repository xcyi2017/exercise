# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 19:07:06 2018

@author: xcy
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1.5, 1.5, 10000)
y = pow(x, 10) + 2*x + 1

plt.plot(x,y)
plt.show()