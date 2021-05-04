import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))

    #Draw a line in frame
    "IN OpenCV coordinate start from top right of computer screen as orgin(0,0) and to the right its x-axis and to the bottom its y-axis"

    img = cv2.line(frame, (0,0), (width,height), (255,0,0), 10)

#cv2.line used to draw line 
#   here
     
#        frame  = source image 
#        (0,0)  = starting position
#        (width,height) = ending position
#        (255,0,0) = color of line 
#         10 = line thickness 

#DRAW LINE ON TOP OF ANOTHER

    img = cv2.line(img, (0,height), (width,0), (0,255,0), 10) #here i pass a line just above blue line by chaning frame as img  as source image 
    

       

    cv2.imshow("Video",img)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()