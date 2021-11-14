#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 02:59:12 2021

@author: yin
"""

#Cited from: https://www.geeksforgeeks.org/convert-image-to-binary-using-python/

import cv2
  
# read the image file
img = cv2.imread('b.png', 2)
  
ret, bw_img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
# converting to its binary form
bw = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
  
cv2.imshow("Binary", bw_img)
cv2.waitKey(0)
cv2.destroyAllWindows()