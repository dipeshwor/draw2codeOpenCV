# import the necessary packages
import imutils
import numpy as np
import cv2

# Open Camera
capture = cv2.VideoCapture(0)

# load the watermark image, making sure we retain the 4th channel
# which contains the alpha transparency
watermark = cv2.imread('images/colorOutline.png', -1)
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

count=0

while True:
	count+=1
	if count>190:
		count=0
	print(count)
	# Capture frames from the camera
	ret, image = capture.read()
	image=cv2.flip(image,1)

	# load the input image, then add an extra dimension to the
	# image (i.e., the alpha transparency)
	(h, w) = image.shape[:2]
	image = np.dstack([image, np.ones((h, w), dtype="uint8") * 255])
	# construct an overlay that is the same size as the input
	# image, (using an extra dimension for the alpha transparency),
	# then add the watermark to the overlay in the bottom-right
	# corner
	overlay = np.zeros((h, w, 4), dtype="uint8")
	overlay[h - wH - 10-count:h - 10-count, w - wW - 10-count:w - 10-count] = watermark
	# blend the two images together using transparent overlays
	output = image.copy()
	cv2.addWeighted(overlay, 1, output, 1.0, 0, output)

	# Show required images
	cv2.imshow("Gesture", output)
	
	# Close the camera if 'q' is pressed
	if cv2.waitKey(1) == ord('q'):
	    break

capture.release()
cv2.destroyAllWindows()