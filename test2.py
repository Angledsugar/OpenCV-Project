import numpy as np
import cv2
def img_load():
    img = cv2.imread('sks.png',cv2.IMREAD_COLOR)
    gray = cv2.imread('sks.png',cv2.IMREAD_GRAYSCALE)
    gray2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cv2.imshow('SKS',img)
    cv2.imshow('gray_SKS',gray)
    cv2.imshow('gray_SKS2', gray2)
    k = cv2.waitKey(0)&0xFF

    if k == 27:
        cv2.destroyAllWindows()

img_load()