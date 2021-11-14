#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:38:32 2021

@author: yinjunze
"""

import matplotlib.pyplot as pl
import numpy as np

# change y1 to the fractal dimensions that you calculated by the box-counting method, y2 to the ones calculated by the radial method, x to the years
y1 = np.array([1.475, 1.493, 1.483, 1.475, 1.457, 1.472, 1.487, 1.477, 1.488, 1.488, 1.476, 1.476, 1.510, 1.570, 1.572, 1.548, 1.547, 1.525, 1.559, 1.479, 1.496])
y2 = np.array([1.541, 1.564, 1.531, 1.477, 1.492, 1.506, 1.544, 1.549, 1.550, 1.522, 1.488, 1.494, 1.599, 1.635, 1.636, 1.613, 1.622, 1.614, 1.688, 1.564, 1.618])
x = np.array(list(range(2000,2021)))

# change the name, x label, and y label of the graph you want to generate.
pl.title('Fractal Dimension of Boston from 2000 to 2020')
pl.xlabel(r'years')
pl.ylabel(r'fractal dimension')

y1label = 'box-counting method'
y2label = 'radial method'

pl.plot(x, y1, 'o')
pl.plot(x, y2, 'o')

# generate the linear regression line 
m1, b1 = np.polyfit(x, y1, 1) 
m2, b2 = np.polyfit(x, y2, 1) 
pl.plot(x, m1*x + b1, 'b', label=y1label) 
pl.plot(x, m2*x + b2, 'y', label=y2label) 

pl.legend()