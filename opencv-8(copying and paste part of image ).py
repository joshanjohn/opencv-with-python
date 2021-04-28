import cv2

img = cv2.imread('assets/logo.png',-1)

#select part of image (by selecting rows and column pixels colors)
tag = img[500:700,600:900]     #copy from row 500 to row 700(not include 700),column 600 to 900

#   Paste the image where there is same pixel gap
img[100:300,650:950] = tag    #replace the slice of [100:300,650:950] by tag 

img = cv2.resize(img,(400,400))
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()