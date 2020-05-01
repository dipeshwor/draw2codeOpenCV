import cv2 
import numpy as np 
import imutils

img = cv2.imread("images/jumbo4.jpg")
img = imutils.resize(img,width=400)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

v = hsv[:,:,2]
th, threshed = cv2.threshold(v, 100, 255, cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
threshed[-1] = 255

cnts = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]

mask = np.zeros_like(threshed)
cv2.drawContours(mask, cnts, -1, (255, 0, 0), -1, cv2.LINE_AA)
mask = cv2.erode(mask, np.ones((3,3), np.int32), iterations=1)

png = np.dstack((img, mask))

cv2.imwrite("images/colorOutline.png", png)