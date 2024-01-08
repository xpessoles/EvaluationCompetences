# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 19:08:56 2022

@author: xpess
"""

suffixe = '_DS_01.pdf'
import os
os.listdir()
L = os.listdir()
for f in L :
    if "pdf" in f:
        f2=f[:-4]+suffixe

        os.rename(f,f2)