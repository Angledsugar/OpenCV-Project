import numpy as np
import cv2

def showcam():
    try:
        print('open cam')
        cap = cv2.VideoCapture(0)
    except:
        print('Not working')
        return
    cap.set(3, 480)
    cap.set(4, 320)

    while True:
        ret, frame = cap.read()

        cv2.imshow('cam_load', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

showcam()