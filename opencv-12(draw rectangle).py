import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()

    width = int(cap.get(3))
    height = int(cap.get(4))

    #DRAW RECTANGELE IN FRAME

    rect = cv2.rectangle(frame, (100,100), (200,200),(255,0,0), -1)

# cv2.rectangle() use to draw rectanle on screen
#   here
#       frame = source image 
#       (100,100) = center position
#       (200,200) = radius
#       (255,0,0) = color
#               5 = rectangle thickness
#insted of 5 we use -1 ti fill entire rectangle
#rect = cv2.rectangle(frame, (100,100), (200,200),(255,0,0), -1)

    cv2.imshow('image',rect)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()