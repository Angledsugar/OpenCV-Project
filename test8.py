import numpy as np
import cv2

lowerBound = np.array ([ 108 , 62 , 146 ])
upperBound = np.array ([ 118 , 105 , 203 ])


def showcam ():
    try:
        print ('open cam ')
        cap = cv2.VideoCapture(0)
    except:
        print ('Not working ')
        return
    cap.set (3, 480 )
    cap.set (4, 320 )

    while True :
        ret, frame = cap.read ()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        color_mask = cv2.inRange( hsv , lowerBound , upperBound )
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT , (5, 5))
        opening = cv2.morphologyEx( color_mask , cv2.MORPH_OPEN , kernel )
        ret1, thr = cv2.threshold( opening , 127 , 255 , 0)
        _, contours, _ = cv2.findContours( thr , cv2.RETR_TREE , cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            for i in range(len(contours)):
                # Get area value
                area = cv2.contourArea( contours [i])
                if area > 1000 : # minimum yellow area
                    rect = cv2.minAreaRect( contours [i])
                    (x, y), (w, h), angle = cv2.minAreaRect( contours [i])
                    center_x = int (x)
                    center_y = int (y)
                    box = cv2.boxPoints( rect )
                    box = np.int0( box )
                    cv2.drawContours( frame , [box ], 0, (0, 0, 255 ), 2)
                    cv2.putText( frame , 'Card ', (center_x , center_y ))
        if not ret:
            print('error ')
            break
        cv2.imshow('bitwise ', color_mask)
        cv2.imshow('cam_ load ', frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
showcam()
