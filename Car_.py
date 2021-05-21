
# Yellow H 54,15 / S 240,125 / V 255,105
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
        ret,frame = cap.read() # camera read and put ret, frame
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # Color Image
        color_mask = cv2.inRange(hsv, lowerBound, upperBound) # Select THing
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5)) # ?
        opening = cv2.morphologyEx(color_mask, cv2.MORPH_OPEN, kernel) # Delete Noise
        ret1, thr = cv2.threshold(opening, 127, 255, 0) # Window size 127x255
        _, contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # Distinguish image(Blue Line)
        # cv2.drawContours(frame, contours, -1, (0, 255, 0), 3)

        if len(contours) > 0:
                for i in range(len(contours)):
                    # Get area value
                    area = cv2.contourArea(contours[i])
                    if area > 1000:  # minimum area
                        rect = cv2.minAreaRect(contours[i])
                        (x, y), (w, h), angle = cv2.minAreaRect(contours[i])
                        box = cv2.boxPoints(rect)
                        box = np.int0(box)
                        # center_x = int(x)
                        # center_y = int(y)
                        #cv2.drawContours(frame, [box], -1, (0, 0, 255), CV_FILLED)
                        box = sorted(box, key=lambda box: box[1])

                        x_1 = int(box[0][0] / 2 + box[1][0] / 2)
                        y_1 = int(box[0][1] / 2 + box[1][1] / 2)
                        x_2 = int(box[2][0] / 2 + box[3][0] / 2)
                        y_2 = int(box[2][1] / 2 + box[3][1] / 2)

                        cv2.line(frame, (x_1, y_1), (x_2, y_2), (0, 255, 0), 2)
                        cv2.line(frame, (x_2, 0), (x_2, 488), (0, 0, 255), 2)

                        if x_1 > x_2 :
                            print('right')
                        else:
                            print('left')

                        cv2.circle(frame, (box[0][0], box[0][1]), 3, (0, 0, 255), -1)
                        cv2.circle(frame, (box[1][0], box[1][1]), 3, (0, 0, 255), -1)
                        cv2.circle(frame, (box[2][0], box[2][1]), 3, (0, 0, 255), -1)
                        cv2.circle(frame, (box[3][0], box[3][1]), 3, (0, 0, 255), -1)
                        #cv2.putText(frame, 'Blue_LIne', (center_x, center_y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)
        cv2.imshow('bitwise',color_mask)
        cv2.imshow('cam_load',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

showcam()

