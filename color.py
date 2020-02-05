import cv2
import numpy as np 

def findCentre(frame,initial_pos):
    centre = initial_pos
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    low_green  = np.array([35, 52, 50])
    high_green = np.array([70, 255, 230])

    # Red color
    low_red  = np.array([161, 155, 84])
    high_red = np.array([179, 255, 255])

    mask = cv2.inRange(hsv,low_green,high_green)
    mask = cv2.medianBlur(mask,3)
    #mask = cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    #mask = cv2.morphologyEx(mask,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))

    contours,hierarchy = cv2.findContours(mask.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        if cv2.contourArea(cnt)>=600:

            (x,y),radius = cv2.minEnclosingCircle(cnt)
            centre = (int(x),int(y))
            radius = int(radius)
            cv2.circle(frame,centre,radius,(0,0,255),2)
            cv2.circle(frame,centre,2,(0,0,255),2)

    #cv2.imshow("mask",mask)
    cv2.imshow("frame",frame)

    return centre
    