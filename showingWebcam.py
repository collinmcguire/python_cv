import numpy as np
import cv2 as cv

## Load image
cam = cv.VideoCapture(2)

## Show the camera
while(1):
	_,frame = cam.read()
	cv.imshow("window", frame)
	if cv.waitKey(5)==27:
		break
cv.destroyAllWindows()