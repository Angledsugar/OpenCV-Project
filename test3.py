import numpy as np
import cv2
import matplotlib.pyplot as plt
def img_load():
    img = cv2.imread('sks.png',cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('SKS',img)
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()

    k = cv2.waitKey(0)&0xFF
    if k == 27:
        cv2.destroyAllWindows()
img_load()