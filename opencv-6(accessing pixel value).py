import cv2

image  = cv2.imread('assets/logo.png',-1)
#pixel of row
print(image[0]) # src[row] to get fist row of image pixel value

#pixel of perticular in a row
print(image[0][45])

# pixel between
print(image[257][45:400])  # [45:400] represent pixel between 45 and 400
