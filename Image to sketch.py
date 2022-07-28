# -*- coding: utf-8 -*-
"""
Created on Thu Jul  7 19:05:58 2022

@author: rupik
"""
import cv2

# Show contour of image using canny filter
img= cv2.imread("C:/Users/rupik/Documents/Edu labs/child.jpg")
print(img)
print(img.shape)

#display the image
cv2.imshow('frame1',img)

# convert bgr to grey
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,70,90)
edges_high = cv2.Canny(gray,230,60)
print(gray.shape)
print(gray)

cv2.imshow('grey',gray)
cv2.imshow('edges',edges)
cv2.imshow('edges2',edges_high)




# wait for any key
cv2.waitKey(0)
# CLose all the frames
cv2.destroyAllWindows()