##opencv_trafficlight_task2_KimTaeYop
# 우선순위 빨-노-초
import cv2
import numpy as np
import time

# 웹캠으로 비디오 캡쳐
cap = cv2.VideoCapture(0)

while (1):
    _, img = cap.read()

    # RGB를HSV로 바꿈
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # 빨간색 범위 정의...
    red_lower = np.array([0, 168, 160], np.uint8)
    red_upper = np.array([72, 255, 208], np.uint8)

    # 파란색 범위 정의...완료
    blue_lower = np.array([103, 112, 0], np.uint8)
    blue_upper = np.array([115, 255, 119], np.uint8)

    # 노란색 범위 정의...완료
    yellow_lower = np.array([12, 213, 140], np.uint8)
    yellow_upper = np.array([31, 255, 255], np.uint8)

    # 이미지에서 범위내 색 찾기
    red = cv2.inRange(hsv, red_lower, red_upper)
    blue = cv2.inRange(hsv, blue_lower, blue_upper)
    yellow = cv2.inRange(hsv, yellow_lower, yellow_upper)

    # kernal 및 색, res 정의
    kernal = np.ones((5, 5), "uint8")  # 데이터 팽창을 위한 kernal값 정의

    red = cv2.dilate(red, kernal)  # 이미지 팽창
    res_r = cv2.bitwise_and(img, img, red)  # 이진 비교함수 bitwise사용

    blue = cv2.dilate(blue, kernal)
    res_b = cv2.bitwise_and(img, img, blue)

    yellow = cv2.dilate(yellow, kernal)
    res_y = cv2.bitwise_and(img, img, yellow)

    # contours정의
    (contours_r, hierarchy_r) = cv2.findContours(red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (contours_b, hierarchy_b) = cv2.findContours(blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (contours_y, hierarchy_y) = cv2.findContours(yellow, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    judge = 0  # 0은 없을때, 1은 파랑, 2는 빨강, 3은 노랑
    ##########미완성 반복###########
    # 다음의 빨, 노, 파 반복문은 순서가 중요하다. 빨간색은 보이면 항상 디텍팅하고, 그다음 노랑, 파랑 순으로
    # judge의 우선순위가 떨어진다.
    ##########
    for pic, contour in enumerate(contours_r):
        judge = 1  # 우선순위를 둘수 있다. 빨강이면 judge가 1
        area = cv2.contourArea(contour)
        if (area > 1500):
            x, y, w, h = cv2.boundingRect(contour)
            if judge <= 1:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.putText(img, "RED color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255))
                print('STOP')
                cv2.imshow("traffic light", img)
                time.sleep(1)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
            break
    ##########
    for pic, contour in enumerate(contours_y):
        judge = 2  # 우선순위를 둘수 있다. 노랑이면 judge가 2
        area = cv2.contourArea(contour)
        if (area > 1500):
            x, y, w, h = cv2.boundingRect(contour)
            if judge <= 2:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 200, 200), 2)
                cv2.putText(img, "YELLOW color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200))
                print('Wait')
                cv2.imshow("traffic light", img)
                time.sleep(1)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
            break
    ##########
    for pic, contour in enumerate(contours_b):
        judge = 3  # 우선순위를 둘수 있다. 파랑이면 judge가 3
        area = cv2.contourArea(contour)
        if (area > 1500):
            x, y, w, h = cv2.boundingRect(contour)
            if judge <= 3:
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(img, "Blue color", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0))
                print('GO')
                cv2.imshow("traffic light", img)
                time.sleep(1)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
            break
    ##########
##########################
#    print('judge:')
#    print(judge)