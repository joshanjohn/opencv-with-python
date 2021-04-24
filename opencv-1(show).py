import cv2
#imread - reading image 
'mode'
# -1 = IMREAD_COLOR
#  0 = IMREAD_GRAYSCALE
#  1 = IMREAD_UNCHANGED

img = cv2.imread('assets/logo.png',0)

#imshow = show image in window
cv2.imshow('sample',img) #sample is wiindow name, img is src

#wait to close a amount of time or we press any key
cv2.waitKey(0) #we use 0 for infinite time 

# close all  window 
cv2.destroyAllwindows()