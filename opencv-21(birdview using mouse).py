import cv2
import numpy as np

img = cv2.imread('assets/book.jpg')

circles = np.zeros((4,2),np.int)
#(4,2) we have 4 points each have x and y
count = 0

def mousePoint(event,x,y,flags,params):
    global count

    if event == cv2.EVENT_LBUTTONDOWN:  #check for left click
        circles[count] = x,y #store value of x,y
        count +=1   #count no: of clicks
        print(circles) 


while True:

    if count == 4:
        width,height = 250,350
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        output = cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("output",output)


    for x in range(0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)

    img = cv2.resize(img,(400,400))
    cv2.imshow("image",img)
    cv2.setMouseCallback("image",mousePoint)    #callbackfuntion
    cv2.waitKey(1)
 