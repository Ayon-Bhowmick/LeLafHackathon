import time
import  numpy as np
import cv2

cam = cv2.VideoCapture(0)

ret, image = cam.read()
cv2.imshow('Imagetest.jpg',image)
cv2.imwrite('/test', image)
cam.release()
cv2.destroyAllWindows()