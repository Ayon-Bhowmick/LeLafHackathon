import RPi.GPIO as GPIO
from time import sleep, time
import cv2

PIN_R = 3
PIN_GREEN = 11
PIN_TRIG = 12
PIN_ECHO = 18

def distance():
    # set Trigger to HIGH
    GPIO.output(PIN_TRIG, True)

    # set Trigger after 0.01ms to LOW
    sleep(0.00001)
    GPIO.output(PIN_TRIG, False)

    StartTime = time()
    StopTime = time()

    # save StartTime
    while GPIO.input(PIN_ECHO) == 0:
        StartTime = time()

    # save time of arrival
    while GPIO.input(PIN_ECHO) == 1:
        StopTime = time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2

    return distance

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_R, GPIO.OUT)
    GPIO.setup(PIN_GREEN, GPIO.OUT)
    GPIO.setup(PIN_TRIG, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    while 1:
        dist = distance()
        if dist < 10:
            GPIO.output(PIN_R, GPIO.HIGH)
            GPIO.output(PIN_GREEN, GPIO.LOW)
        else:
            GPIO.output(PIN_R, GPIO.LOW)
            GPIO.output(PIN_GREEN, GPIO.HIGH)

except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
