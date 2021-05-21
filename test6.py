import cv2
import numpy as np

img = cv2.imread('sks.png', cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 127, 255, 0)


cv2.imshow('sks', img)
cv2.imshow('sks_thresh',thresh)
cv2.waitKey(0)