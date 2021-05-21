import numpy as np
import cv2

lowerBound = np.array([105, 61, 43])
upperBound = np.array([154, 255, 255])

def showcam():
    try:
        cap = cv2.VideoCapture(0)
        print('open cam')
    except:
        print ('Not working')
        return
    cap.set(7, 480)
    cap.set(6, 320)
    while True:
        ret,frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_mask = cv2.inRange(hsv, lowerBound, upperBound) #Select THing
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
        opening = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, kernel) # Delete Noise
        ret1, thr = cv2.threshold(opening, 127, 255, 0)
        _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)
        if len(contours) > 0:
                for i in range(len(contours)):
                    # Get area value
                    area = cv2.contourArea(contours[i])
                    if area > 1000:  # minimum area
                        rect = cv2.minAreaRect(contours[i])
                        (x, y), (w, h), angle = cv2.minAreaRect(contours[i])
                        center_x = int(x)
                        center_y = int(y)
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)
                        cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)
                        cv2.putText(frame, 'Blue_LIne', (center_x, center_y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
        cv2.imshow('bitwise',color_mask)
        cv2.imshow('cam_load',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()
showcam()
