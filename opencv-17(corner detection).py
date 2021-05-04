#set a circle of blue color in every corner in chessboard

import numpy as np
import cv2
 

img = cv2.imread('assets/chessboard.png')
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

#for detection we need to convert image into gray scale color
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#   Here we use shi-Tomasi corner detectionand good feature to track algorithm. for more, check out link bellow
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_feature2d/py_shi_tomasi/py_shi_tomasi.html#shi-tomasi

corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# Here,
#   gray = source image
#   100 = number of corners
#   0.01 = minimum quality(range from 0 to 1[0- 0%confidence,1- 100%confidence])   
#   10 = minimum euclidean distance(absolute distance between two points)

corners = np.int0(corners)  #make as numpy array and turn floating points to integers

for corner in corners:      #access each points
    x,y = corner.ravel()    #ravel is used to change a 2-dimensional array or a multi-dimensional array into a contiguous flattened array.
    #i.e, 
    #   if we have [[[1,2,3]]] -> [1,2,3]
    #   if we have [[1,2], [1,2]] -> [1,2,1,2]
    cv2.circle(img, (x,y), 5, (255,0,0), -1)





cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()