import cv2
import numpy as np

img = cv2.imread('sks.png', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)
_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours, -1, (0, 255, 0), 3)

cv2.imshow('sks', img)
cv2.imshow('sks_contours', thresh)
cv2.waitKey(0)

