import time
import  numpy as np
import cv2
import RPi.GPIO as GPIO

try:
    GPIO.setmode(GPIO.BOARD)

    PIN_TRIGGER = 18
    PIN_ECHO = 24
    PIN_REDLED = 13
    PIN_YELLOWLED = 16
    PIN_GREENLED = 17


    GPIO.setup(PIN_TRIGGER, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    print ("Waiting for sensor to settle")

    time.sleep(2)

    print ("Calculating distance")

    GPIO.output(PIN_TRIGGER, GPIO.HIGH)

    time.sleep(0.00001)

    GPIO.output(PIN_TRIGGER, GPIO.LOW)

finally:
      GPIO.cleanup()

cam = cv2.VideoCapture(0)

ret, image = cam.read()
cv2.imshow('imagetest.jpg',image)
cv2.imwrite('imagetest.jpg', image)
cam.release()
cv2.destroyAllWindows()

# !! connect to ericks junk here

response = [0, "hellow world"]

if(response[0] == 0):
     print("is trash")
     GPIO.output(PIN_REDLED, GPIO.HIGH)
if(response[1] == 0):
     print("is recycling")
     GPIO.output(PIN_GREENLED, GPIO.HIGH)
if(response[2] == 0):
     print("error")
     GPIO.output(PIN_YELLOWLED, GPIO.HIGH)
time.sleep(5)

print(response[1])
