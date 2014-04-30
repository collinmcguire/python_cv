import numpy as np
import cv2 as cv

## Create a window
##cv.namedWindow("window", cv.CV_WINDOW_AUTOSIZE)
##cv.moveWindow("window", 100, 100)

## Load image
cam = cv.VideoCapture(2)

## Show the camera
while(1):
	_,frame = cam.read()
	cv.imshow("window", frame)
	if cv.waitKey(5)==27:
		break
cv.destroyAllWindows()