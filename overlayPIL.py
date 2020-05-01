import cv2 
import numpy as np 
import imutils
from PIL import Image
import time

img = Image.open("images/colorOutline.png")
# resize the image
size = (int(img.size[0]*0.5), int(img.size[1]*0.5))
#print(size)
img = img.resize(size,Image.ANTIALIAS)

background = Image.open("images/tufts2.jpg")
#print(background.size[0]/2, background.size[1]/2)
# resize the image
size = (int(background.size[0]*0.6), int(background.size[1]*0.6))
#print(size)
background = background.resize(size,Image.ANTIALIAS)

#print(background.size)

background.paste(img, (100, 300), img)
background.save('images/output.png',"PNG")
output = cv2.imread('images/output.png')
cv2.imshow('Output', output) 
#time.sleep(0.5)

cv2.waitKey()
cv2.destroyAllWindows() 