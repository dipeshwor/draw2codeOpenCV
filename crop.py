import cv2 
import numpy as np 
import imutils

fname = "jumbo.jpg"
img = cv2.imread(fname)
img = imutils.resize(img,width=400)

y = 80 
x = 30
h = 380
w = 380

crop_img = img[y:y+h, x:x+w]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)