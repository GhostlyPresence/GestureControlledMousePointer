
import cv2
import numpy as np 
import pyautogui as gui
from color import findCentre

#returns error if pointer moves to position (0,0)
gui.FAILSAFE =True

#default webcam
cap = cv2.VideoCapture(0)

for i in range(20):
    ret,frame = cap.read()
#print("frame = ",frame.shape[0:2])

while ret:
    c = gui.position()
    screenWidth, screenHeight = gui.size()
    dim = (screenWidth//3,screenHeight//3)
    ret,frame = cap.read()
    frame = np.flip(frame,axis=1)
    frame = cv2.resize(frame,dim)

    (x,y) = findCentre(frame,c)
    if not (x==c[0] and y==c[1]):
        x=3*x
        y=3*y

    print(c,(x,y))
    try:
        gui.moveTo(x,y,0)
    except:
        pass  

    if cv2.waitKey(5) == 27:
        break

cap.release


