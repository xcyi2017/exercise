# -*- coding: utf-8 -*-
"""
Created on Mon Sep 17 12:37:13 2018

@author: xcy
"""

import numpy as np
def isEqual(d1, d2):
    if (abs(d1-d2)<1e-7):
        return True
    else:
        return False
    
def nearDistance(s0,s1,t0,t1):
    x1, y1, z1 = s0
    x2, y2, z2 = s1
    x3, y3, z3 = t0
    x4, y4, z4 = t1
    
    ux = x2 - x1
    uy = y2 - y1
    uz = z2 - z1

    vx = x4 - x3
    vy = y4 - y3
    vz = z4 - z3

    wx = x1 - x3
    wy = y1 - y3
    wz = z1 - z3

    a = (ux * ux + uy * uy + uz * uz)#u*u
    b = (ux * vx + uy * vy + uz * vz)#u*v
    c = (vx * vx + vy * vy + vz * vz)#v*v
    d = (ux * wx + uy * wy + uz * wz)#u*w 
    e = (vx * wx + vy * wy + vz * wz)#v*w
    dt = a * c - b * b
    
    

    sd = dt
    td = dt

    sn = 0.0#sn = be-cd
    tn = 0.0#tn = ae-bd
    
    if (isEqual(dt, 0.0)):
        #两直线平行
        sn = 0.0#在s上指定取s0
        sd = 1.00#防止计算时除0错误

        tn = e#/求tc
        td = c
    else:
        sn = (b * e - c * d)
        tn = (a * e - b * d)
        if sn<0.0:
            #最近点在s起点以外，同平行条件
            sn = 0.0
            tn = e
            td = c
        elif sn>sd:
            #最近点在s终点以外(即sc>1,则取sc=1)
            sn = sd
            tn = e + b
            td = c
    if tn<0.0:
        #最近点在t起点以外
        tn = 0.0
        if (-d < 0.0):#如果等号右边小于0，则sc也小于零，取sc=0
            sn = 0.0
        elif (-d > a):#如果sc大于1，取sc=1
            sn = sd
        else:
            sn = -d
            sd = a
    elif tn>td:
        tn = td
        if (-d + b) < 0.0:
            sn = 0.0
        elif (-d + b) > a:
            sn = sd
        else:
            sn = (-d + b)
            sd = a
            
    sc = 0.0
    tc = 0.0
    if (isEqual(sn, 0.0)):
        sc=0.0
    else:
        sc = sn/sd
        
    if isEqual(tn, 0.0):
        tc =0.0
    else:
        tc = tn/td
        
    dx = wx + (sc * ux) - (tc * vx)
    dy = wy + (sc * uy) - (tc * vy)
    dz = wz + (sc * uz) - (tc * vz)
    return np.sqrt(dx * dx + dy * dy + dz * dz)
        
    
        
    