import cv2
import numpy as np

framewidth = 640
frameheight = 480
cap = cv2.VideoCapture(0)
cap.set(3,framewidth)
cap.set(4,frameheight)

def empty(a):
    pass

#create Tackbar
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",641,240)
cv2.createTrackbar("HUE Min","HSV",0,179,empty)     #here empty is a simple funtion 
cv2.createTrackbar("HUE Max","HSV",179,179,empty)
cv2.createTrackbar("SAT Min","HSV",0,255,empty)
cv2.createTrackbar("SAT Max","HSV",255,255,empty)
cv2.createTrackbar("VALUE Min","HSV",0,255,empty)
cv2.createTrackbar("VALUE Max","HSV",255,255,empty)



while True:
    ret,img = cap.read()
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #get a range of colors

    #Getting each values from trackbar
    h_min = cv2.getTrackbarPos("HUE Min","HSV")
    h_max = cv2.getTrackbarPos("HUE Max","HSV")
    s_min = cv2.getTrackbarPos("SAT Min","HSV")
    s_max = cv2.getTrackbarPos("SAT Max","HSV")
    v_min = cv2.getTrackbarPos("VALUE Min","HSV")
    v_max = cv2.getTrackbarPos("VALUE Max","HSV")

    #Putting values in matrixs
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    #create mask from these values
    mask =cv2.inRange(imgHsv,lower,upper)
    result = cv2.bitwise_and(img,img, mask = mask)

    #convert color Gray into BGR
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    #stack images
    hStack = np.hstack([img,mask,result])

    #cv2.imshow("image",img)
    #cv2.imshow("HSVimg",imgHsv)
    #cv2.imshow("Mask", mask)
    #cv2.imshow("Result", result)
    hStack = cv2.resize(hStack,(0,0),fx=0.5,fy=0.5)
    cv2.imshow("stacked",hStack)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()