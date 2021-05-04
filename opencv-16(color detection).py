#detect only blue color 

import cv2
import numpy as np

cap  = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #cv2.cvtColor will convert the color format
#     cv2.cvtColor([source image,cv2.[COLOR_[colorformat]2[colorformat])

    lower_blue = np.array([90, 50, 50])    #lighter blue
    upper_blue = np.array([130, 255, 255])  #dark blue

    # masks - part of an image 

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    #this return new image or maks of an image which has only the blue pixels existing

    result = cv2.bitwise_and(frame, frame, mask=mask)
    "this bitwise_and will take source image and second source image and blend them together using mask"
    

    cv2.imshow('color',result)
    cv2.imshow('mask',mask)
    

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()