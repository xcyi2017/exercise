# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 17:29:09 2018

@author: xcy
"""

import numpy as np

class pso:
    
    def __init__(self):
        self.mean_ = None
        self.std_ = None
        
    def fit(self):
        self.mean_ = 1
        self.std_ = 2
        return self