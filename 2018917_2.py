# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 14:22:43 2018

@author: xcy
"""
import numpy as np
def dist3D_Segment_to_Segment(s0,s1,t0,t1):
    small_num = 1e-7
    u = s1 - s0
    v = t1 - t0
    w = s0 - t0
    
    a = np.dot(u, u)
    b = np.dot(u, v)
    c = np.dot(v, v)
    d = np.dot(u, w)
    e = np.dot(v, w)
    
    D = a*c -b*b
    sc=sN=sD = D
    tc=tN=tD = D
    
    if D<small_num:
        sN = 0.0
        sD = 1.0
        tN = e
        tD = c
    else:
        sN = b*e - c*d
        tN = a*e - b*d
        if sN < 0.0:
            sN = 0.0
            tN = e
            tD = c
        elif sN >sD:
            sN = sD
            tN = e + b
            tD = c
    if tN<0.0:
        tN=0.0
        if -d < 0.0:
            sN = 0.0
        elif -d > a:
            sN = sD
        else:
            sN = -d
            sD = a
    elif tN>tD:
        tN = tD
        if (-d + b) < 0.0:
            sN = 0
        elif (-d + b) > a:
            sN = sD
        else:
            sN = -d +  b
            sD = a
            
    sc = 0.0 if abs(sN)<small_num else sN/sD
    tc = 0.0 if abs(tN)<small_num else tN/tD
        
    dP = w+(sc*u)-(tc*v)
    return np.linalg.norm(dP)
        
    