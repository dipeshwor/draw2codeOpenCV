import cv2 
import numpy as np 
import imutils

image = cv2.imread('jumbo.jpg')
image = imutils.resize(image,width=400)
original = image.copy()
h, w, _ = image.shape

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15,1))
close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

cnts = cv2.findContours(close, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
minimum_area = .75 * h * w
cnts = [c for c in cnts if cv2.contourArea(c) < minimum_area]
cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    #ROI = 255 - original[y:y+h, x:x+w]
    ROI = original[y:y+h, x:x+w]
    cv2.rectangle(image, (x, y), (x + w, y + h), (36,255,12), 2)
    break

cv2.imwrite('roi.jpg', ROI)


fname = "jumbo2.jpg"
img = cv2.imread(fname)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

v = hsv[:,:,2]
th, threshed = cv2.threshold(v, 100, 255, cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
threshed[-1] = 255

cnts = cv2.findContours(threshed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]

mask = np.zeros_like(threshed)
cv2.drawContours(mask, cnts, -1, (255, 0, 0), -1, cv2.LINE_AA)
mask = cv2.erode(mask, np.ones((3,3), np.int32), iterations=1)

png = np.dstack((img, mask))
cv2.imwrite("alpha.png", png)
