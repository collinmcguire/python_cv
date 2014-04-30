import numpy as np
import cv2 as cv

## Create a window
cv.namedWindow("window", cv.CV_WINDOW_AUTOSIZE)
cv.moveWindow("window", 100, 100)

## Load image
im = cv.imread("test.jpg")

## Show the image
def showWindow(message):
	cv.imshow("window", im)
	cv.waitKey(10000)

showWindow("Testing")