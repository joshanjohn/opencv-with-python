import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret,frame = cap.read()
    width = int(cap.get(3)) #   cap.get(3) return width of the video, 3 is identifier
    height = int(cap.get(4))

    #Pasting image from frame to a numpy array,inside we pass the shape(row,column,shape) 

    image = np.zeros(frame.shape,np.uint8)  # we pass same shape on frame,type of the frame .so here we have black screen with same shape as frame
        #uint8 = unsigned integer 8 bits

    "now shrink the image(frame)"
    smaller_frame = cv2.resize(frame,(0,0),fx=0.5,fy=0.5) # resize exactly half 

    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #top left
    image[height//2:, :width//2] = smaller_frame    #bottom left
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)  #top right
    image[height//2:, width//2:] = smaller_frame    #bottom right

    cv2.imshow('Multiply Mirror',image) 
    #cv2.imshow('Multiply Mirror',frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()