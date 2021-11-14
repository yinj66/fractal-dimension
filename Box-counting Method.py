#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 20:42:05 2021

@author: yinjunze
"""

#The function (fractal_dimension) in this section is adapted from: 
#https://gist.github.com/viveksck/1110dfca01e4ec2c608515f0d5a5b1d1, written by 
#Viveksck. Viveksck used a library called scipy.misc, but that library did not 
#work in my computer even though I downloaded, so I changed some of the code in 
#that function and used matplotlib.pyplot instead.

import numpy as np
import matplotlib.pyplot as plt

def fractal_dimension(Z, threshold=0.9):

    # Only for 2d image
    assert(len(Z.shape) == 2)

    # From https://github.com/rougier/numpy-100 (#87)
    def boxcount(Z, k):
        S = np.add.reduceat(
            np.add.reduceat(Z, np.arange(0, Z.shape[0], k), axis=0),
                               np.arange(0, Z.shape[1], k), axis=1)

        # We count non-empty (0) and non-full boxes (k*k)
        return len(np.where((S > 0) & (S < k*k))[0])


    # Transform Z into a binary array
    Z = (Z < threshold)
    plt.imshow(Z)
    plt.show()

    # Minimal dimension of image
    p = min(Z.shape)

    # Greatest power of 2 less than or equal to p
    n = 2**np.floor(np.log(p)/np.log(2))

    # Extract the exponent
    n = int(np.log(n)/np.log(2))

    # Build successive box sizes (from 2**n down to 2**1)
    sizes = 2**np.arange(n, 1, -1)

    # Actual box counting with decreasing size
    counts = []
    for size in sizes:
        """print(counts)
        print(size)"""
        counts.append(boxcount(Z, size))

    # Fit the successive log(sizes) with log (counts)
    coeffs = np.polyfit(np.log(sizes), np.log(counts), 1)
    return -coeffs[0]

# write the names of the satellite images. Change lista before using
lista = ["2000.jpg","2001.jpg","2002.jpg","2003.jpg","2004.jpg","2005.jpg",
         "2006.jpg","2007.jpg","2008.jpg","2009.jpg","2010.jpg","2011.jpg",
         "2012.jpg","2013.jpg","2014.jpg","2015.jpg","2016.jpg","2017.jpg",
         "2018.jpg","2019.jpg","2020.jpg"]

# for loop is used to calculate the fractal dimension of the images in lista
for i in lista:
    print("box-counting dimension (computed): ", fractal_dimension(plt.imread(i)
          [:,:,1], threshold=0.2))