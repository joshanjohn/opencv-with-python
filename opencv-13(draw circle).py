import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    #DRAW CIRCLE
    circle = cv2.circle(frame, (300,300), 60, (0,0,255), -1)
    #cv.circle use draw circle in frame
# here,
#   frame = source image
#   (300,300) = center position
#   60 = radius
#   (0,0,255) = color
#   -1 = fill color or can use any +ve number to represent circle thickness

    cv2.imshow('image',circle)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()