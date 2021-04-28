import cv2
import random   #for simply get a random color

img = cv2.imread('assets/logo.png',-1)

for i in range(1000): #look through first 100 rows
    for j in range(img.shape[1]):   # to get the entire width of image for the column in i
        
        img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
        #   random.randint(255) generate number between 0 and 255

img = cv2.resize(img,(400,400))
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()