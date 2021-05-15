import cv2
import numpy as np

def mousePoint(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:  #check for left click
        print(x,y)


img = cv2.imread('assets/card.jpg')
cv2.imshow("image",img)

cv2.setMouseCallback("image",mousePoint)
cv2.waitKey(0)