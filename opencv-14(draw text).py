import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    height = int(cap.get(4))
    
    #DRAW TEXT

    font = cv2.FONT_HERSHEY_SIMPLEX #select a font from cv2 documentaion
    #cv.FONT_[FONT STYLE]   allows to select fonts

    text = cv2.putText(frame,'cool man take it easy!', (200,height-10), font, 1, (0,0,0), 5, cv2.LINE_AA)
#cv2.putText() allows to put the text in the base image 
# here,
#   frame = base image 
#   'cool man take it easy!' = text
#   (200,height-10) = center postision
#   font = text font
#   1 = font scale
#   (0,0,0) = color
#   5 =     line thickness
#   cv.LINE_AA = line type

    cv2.imshow('Text',text)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()