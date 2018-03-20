import cv2

import numpy as np
import cv2.cv as cv
cap= cv2.VideoCapture(0)
while 1:
	ret,img = cap.read()
	frame = cv2.resize(img,(600,600))
	cv2.waitKey(1)
