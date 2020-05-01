# import the necessary packages
import imutils
import numpy as np
import cv2

# load the watermark image, making sure we retain the 4th channel
# which contains the alpha transparency
watermark = cv2.imread('images/colorOutline.png', cv2.IMREAD_UNCHANGED)
watermark = imutils.resize(watermark,width=200)
(wH, wW) = watermark.shape[:2]

# split the watermark into its respective Blue, Green, Red, and
# Alpha channels; then take the bitwise AND between all channels
# and the Alpha channels to construct the actaul watermark
# NOTE: I'm not sure why we have to do this, but if we don't,
# pixels are marked as opaque when they shouldn't be

(B, G, R, A) = cv2.split(watermark)
B = cv2.bitwise_and(B, B, mask=A)
G = cv2.bitwise_and(G, G, mask=A)
R = cv2.bitwise_and(R, R, mask=A)
watermark = cv2.merge([B, G, R, A])

# load the input image, then add an extra dimension to the
# image (i.e., the alpha transparency)
image = cv2.imread('images/tufts.jpg')
image = imutils.resize(image,width=600)
(h, w) = image.shape[:2]
image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
# construct an overlay that is the same size as the input
# image, (using an extra dimension for the alpha transparency),
# then add the watermark to the overlay in the bottom-right
# corner
overlay = np.zeros((h, w, 4), dtype="uint8")
#overlay[h - wH - 10:h - 10, w - wW - 10:w - 10] = watermark
overlay[h - wH - 150:h - 150, w - wW - 150:w - 150] = watermark
# blend the two images together using transparent overlays
output = image.copy()
#cv2.addWeighted(overlay, 1, output, 1.0, 0, output)
cv2.addWeighted(overlay, 1, output, 1, 0, output)

# Show required images
cv2.imshow("Output", output)
cv2.waitKey()
cv2.destroyAllWindows() 
#cv2.imwrite('images/merged.png', output)