# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 23:03:43 2019

@author: Mary Mae
"""

import numpy as np
X = np.array([(5,4,3,2,1),(10,9,8,7,6),(15,14,13,12,11),(20,19,18,17,16),(25,24,23,22,21)])
Z = (X-np.mean(X)/np.std(X))