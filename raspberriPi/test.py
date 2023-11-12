import RPi.GPIO as GPIO
from time import sleep

PIN_YELLOW = 16
try:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(PIN_YELLOW, GPIO.OUT)

    GPIO.output(PIN_YELLOW, GPIO.HIGH)
    sleep(10)
    GPIO.output(PIN_YELLOW, GPIO.LOW)
except Exception as e:
    print("error")
finally:
    GPIO.cleanup()
