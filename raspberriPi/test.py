import RPi.GPIO as GPIO
from time import sleep, time

PIN_RED = 33
PIN_YELLOW = 36
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
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(PIN_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    return distance

try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_RED, GPIO.OUT)
    GPIO.setup(PIN_YELLOW, GPIO.OUT)
    GPIO.setup(PIN_GREEN, GPIO.OUT)
    GPIO.setup(PIN_TRIG, GPIO.OUT)
    GPIO.setup(PIN_ECHO, GPIO.IN)

    while 1:
        dist = distance()
        if dist < 10:
            GPIO.output(PIN_RED, GPIO.HIGH)
            GPIO.output(PIN_YELLOW, GPIO.LOW)
            GPIO.output(PIN_GREEN, GPIO.LOW)
        elif dist < 20 and dist > 10:
            GPIO.output(PIN_RED, GPIO.LOW)
            GPIO.output(PIN_YELLOW, GPIO.HIGH)
            GPIO.output(PIN_GREEN, GPIO.LOW)
        else:
            GPIO.output(PIN_RED, GPIO.LOW)
            GPIO.output(PIN_YELLOW, GPIO.LOW)
            GPIO.output(PIN_GREEN, GPIO.HIGH)

except Exception as e:
    print(e)
finally:
    GPIO.cleanup()
