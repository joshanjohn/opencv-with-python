import cv2
image  = cv2.imread('assets/logo.png',-1)
print(image)#get numpy array
#here we have [0 0 0 0] means border of image is black or that hex code color
"""" 
        PIXEL VALUE REPRESENTAION IN OPENCV
    opencv use BGR
    values are between 0-255
    0 = represent none 
    255 = represent all 
    any value like 128 means light"""
print(type(image)) #output: <class 'numpy.ndarray'>

#To return height(rows),width(column),channel(RGB/BGR) in tuple
print(image.shape) #output: (1200, 1200, 4)
print(type(image.shape))