#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 21:17:03 2021

@author: yinjunze
"""


import os
import glob

import cv2
import matplotlib.pyplot as plt
import numpy as np

# before using this code, find the dimension (length and width) of the image, and write the width and length in r, c; write the center of the image in xr, xc.
xr, xc = 450, 720
r, c = np.arange(900), np.arange(1440)
cc, rr = np.meshgrid(c, r)
dr = rr - xr
dc = cc - xc
dd = np.sqrt(dr**2 + dc**2)

def radial_method(Z, ax, threshold=85, title=''):
    bw_img = img > threshold
    
    # used to count the number of pixels
    def pixel_count(bw_img, k):
        ind = dd < k  # circle with i radius
        count = np.sum(bw_img[ind])
        return count
    
    # used to change the radius of the circle
    radius = np.arange(70, 390, 40)

    ax[0].imshow(bw_img, 'gray', vmin=0, vmax=1)
    ax[0].set_title(title)
        
    counts = []
    for radiu in radius:
        counts.append(pixel_count(bw_img, radiu))

    # Fit the successive log(radius) with log (counts)
    coeffs = np.polyfit(np.log(radius), np.log(counts), 1)

    ax[1].plot(np.log(radius), np.log(counts), 'ro')
    x=np.linspace(0, max(np.log(radius)))
    ax[1].plot(x, coeffs[0]*x+coeffs[1], 'g--')
    ax[1].set_title('%s %.3f' % ('radius_method', coeffs[0]))
    
    return coeffs[0]
    
# before using it, change the file name, which contains all of the satellite images, or try to use the function (radial_method) directly to the images.
image_file_paths = glob.glob("./data/a_*.jpg")
image_file_paths.sort()

fig, ax = plt.subplots(len(image_file_paths), 2, figsize=(10, 80))
for i in range(len(image_file_paths)):
    image_file_path = image_file_paths[i]
    img = cv2.imread(image_file_path, 0)
    image_file_basename = os.path.basename(image_file_path)
    radial_method(img, ax[i], 127, image_file_basename)  
plt.show()