import cv2
#imread - reading image 
'mode'
# -1 = IMREAD_COLOR
#  0 = IMREAD_GRAYSCALE
#  1 = IMREAD_UNCHANGED
img = cv2.imread('assets/logo.png',0)
# RESIZE image
img = cv2.resize(img,(400,400)) #'scr,size in tuple'
'rezise by fraction'
#img = cv2.resize(img,(0,0),fx=1,fy=1) 

#ROTATE image

img = cv2.rotate(img,cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)


#imshow = show image in window
cv2.imshow('sample',img) #sample is wiindow name, img is src
#wait to close a amount of time or we press any key
cv2.waitKey(0) #we use 0 for infinite time 
# close all  window 
cv2.destroyAllwindows()