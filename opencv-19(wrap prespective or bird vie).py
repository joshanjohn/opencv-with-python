import cv2 
import numpy as np

img = cv2.imread('assets/card.jpg')

width,height = 250,350

#create a matrics as same as card size
pts1 = np.float32([[359,120],[524,190],[245,324],[432,399]])

#points for bird view image(pts2)
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

output = cv2.warpPerspective(img,matrix,(width,height))

#ploting a circle to identify the point
#cv2.circle(img,(pts1[0][0],pts1[0][1]),5,(0,0,255),cv2.FILLED)

#to have all 4 points
for x in range(0,4):
    cv2.circle(img,(pts1[x][0],pts1[x][1]),6,(0,255,0),cv2.FILLED)

cv2.imshow("Orginal",img)
cv2.imshow("Result",output)
cv2.waitKey(0)