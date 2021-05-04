#HSV - Huge Saturation and Lightness/brightness

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


    cv2.imshow('color',hsv)
    
    

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()