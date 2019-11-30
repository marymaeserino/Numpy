# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 11:56:49 2019

@author: Mary Mae
"""

import numpy as np
A = np.arange(1,101).reshape(10,10)
msqrd = A**2
div = msqrd[msqrd%3 == 0]
print ("")
print("Matrix A:")
print(msqrd)
print("")
print("The elements from the matrix that are divisible by 3 are:")
print("")
print(div)