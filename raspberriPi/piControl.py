import RPi.GPIO as GPIO
from time import sleep, time
import cv2

PIN_TRASH = 3
PIN_REC = 11
PIN_TRIG = 12
PIN_ECHO = 18
cap = cv2.VideoCapture(0)

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
    GPIO.setup(PIN_TRASH, GPIO.OUT)
    GPIO.setup(PIN_REC, GPIO.OUT)
    GPIO.setup(PIN_TRIG, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    while 1:
        dist = distance()
        if dist < 10:
            GPIO.output(PIN_TRASH, GPIO.HIGH)
            GPIO.output(PIN_REC, GPIO.LOW)
            ret, frame = cap.read()
            cv2.imshow("frame", frame)
        else:
            GPIO.output(PIN_TRASH, GPIO.LOW)
            GPIO.output(PIN_REC, GPIO.HIGH)
            cv2.destroyAllWindows()

except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
    cap.release()
    cv2.destroyAllWindows()
