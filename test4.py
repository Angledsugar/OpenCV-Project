import numpy as np
import cv2
import matplotlib.pyplot as plt

def histogram():
    img = cv2.imread('sks.png',cv2.IMREAD_COLOR)
    cv2.imshow('sks',img)
    color = ('b','g','r')
    for i, col in enumerate(color):
        hist1 = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist1,color = col)
        plt.xlim([0, 256])
    plt.show()

    k = cv2.waitKey(0)&0xFF
    if k == 27:
        cv2. destroyAllWindows()

histogram()