import cv2
import numpy as np

b_lowerBound = np.array([100, 127, 70])
b_upperBound = np.array([120, 215, 255])

y_lowerBound = np.array([15, 110, 115])
y_upperBound = np.array([89, 255, 225])

g_lowerBound = np.array([15, 45, 30])
g_upperBound = np.array([140, 165, 190])

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
        ret, frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        b_color_mask = cv2.inRange(hsv, b_lowerBound, b_upperBound)  # Select Thing - Blue
        y_color_mask = cv2.inRange(hsv, y_lowerBound, y_upperBound)  # select Thing - Yellow
        g_color_mask = cv2.inRange(hsv, g_lowerBound, g_upperBound)  # select Thing - Green

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

        b_opening = cv2.morphologyEx(b_color_mask, cv2.MORPH_OPEN, kernel)  # Delete Noise_B
        y_opening = cv2.morphologyEx(y_color_mask, cv2.MORPH_OPEN, kernel)  # Delete Noise_Y
        g_opening = cv2.morphologyEx(g_color_mask, cv2.MORPH_OPEN, kernel)  # Delete Noise_G

        ret_b, thr_b = cv2.threshold(b_opening, 127, 255, 0)
        ret_y, thr_y = cv2.threshold(y_opening, 127, 255, 0)
        ret_g, thr_g = cv2.threshold(g_opening, 127, 255, 0)

        _, contours_b, _ = cv2.findContours(thr_b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _, contours_y, _ = cv2.findContours(thr_y, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        _, contours_g, _ = cv2.findContours(thr_g, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        def color(contours):
            for i in range(len(contours)):
                area = cv2.contourArea(contours[i])
                if area > 1000:
                    rect = cv2.minAreaRect(contours[i])
                    (x, y), (w, h), angle = cv2.minAreaRect(contours[i])
                    box = cv2.boxPoints(rect)
                    box = np.int0(box)
                    center_x = int(x)
                    center_y = int(y)
                    cv2.drawContours(frame, [box], -1, (0, 0, 255), 2)
                    return center_x, center_y

        if len(contours_b) > 0 and len(contours_y) > 0 and len(contours_g):
            cv2.putText(frame, 'Blue', (color(contours_b)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)

        if len(contours_b) > 0 and len(contours_y) > 0:
            cv2.putText(frame, 'Blue', (color(contours_b)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)

        if len(contours_b) > 0 and len(contours_g) > 0:
            cv2.putText(frame, 'Blue', (color(contours_b)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)

        elif len(contours_b) == 0 and len(contours_y) > 0 and len(contours_g) > 0:
            cv2.putText(frame, 'Yellow', (color(contours_y)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)

        elif len(contours_g) > 0:
            cv2.putText(frame, 'Green', (color(contours_g)), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 255), 2)

        else:
            print('not found')

        cv2.imshow('bitwise',b_color_mask)
        cv2.imshow('cam_load',frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

showcam()
