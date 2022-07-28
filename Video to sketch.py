# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 19:22:29 2022

@author: rupik
"""

import cv2

cap = cv2.VideoCapture('C:/Users/rupik/Documents/Edu labs/video.avi')

#display  frame count
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)


while (cap.isOpened()):
    # mif vdo read fram successfully, ret = true
    #frame = frame from vdo
    ret,frame = cap.read()
    frame = cv2.resize(frame,(740,580),fx=200,fy=300,
                       interpolation=cv2.INTER_NEAREST)
    
        
    cv2.imshow('f1',frame)
    # convert bgr to grey
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,60,90)
    edges_high = cv2.Canny(gray,100,200)
    print(gray.shape)
    print(gray)

    cv2.imshow('grey',gray)
    cv2.imshow('edges',edges)
    cv2.imshow('edges2',edges_high)
    
    
    m_blur = cv2.medianBlur(frame,3)
    cv2.imshow('m',m_blur)
    
    k = cv2.waitKey(60) & 0xFF
    if k==ord('q') or k==27:
        break
    
cap.release()
cv2.destroyAllWindows()