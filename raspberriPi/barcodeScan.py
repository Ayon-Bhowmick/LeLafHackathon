from base64 import b64encode
import json
import time
import  numpy as np
import cv2
import RPi.GPIO as GPIO
# from .iot.aws-iot-device-sdk-python-v2.samples.pubsub_img import setInput

from iot.aws_iot_device_sdk_python_v2.samples.pubsub_img import ImgDataService



GPIO.setmode(GPIO.BOARD)

# define all pin numbers for physical electronics
PIN_TRIGGER = 18
PIN_ECHO = 24
PIN_REDLED = 13
PIN_YELLOWLED = 16
PIN_GREENLED = 17

# set up the pins for the distance sensor
GPIO.setup(PIN_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ECHO, GPIO.IN)

GPIO.output(PIN_TRIGGER, GPIO.LOW)

time.sleep(2)

# define webcam
cam = cv2.VideoCapture(0) 

# function which gets the distance from the ultrasonic sensor
def getDistance() -> float:
    # Send a 10us pulse to trigger the sensor
    GPIO.output(PIN_TRIGGER, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(PIN_TRIGGER, GPIO.LOW)

    # Wait for the echo pin to go high (start of pulse)
    while GPIO.input(PIN_TRIGGER) == 0:
        pulse_start = time.time()

    # Wait for the echo pin to go low (end of pulse)
    while GPIO.input(PIN_TRIGGER) == 1:
        pulse_end = time.time()

    # Calculate pulse duration and convert to distance (in cm)
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)

    return distance
def displayMessage(message):
    #display to lcd screen
    print(message)
    return

def generateOutput(category, message):
    
    # check the category classification of the image
    if(category == 0):
        print("is trash")
        GPIO.output(PIN_REDLED, GPIO.HIGH)
    if(category == 1):
        print("is recycling")
        GPIO.output(PIN_GREENLED, GPIO.HIGH)
    if(category == 2):
        print("error")
        GPIO.output(PIN_YELLOWLED, GPIO.HIGH)
        return
    # display the message to the lcd screen
    displayMessage(message)

    #display output for 5 seconds
    time.sleep(5)

    return

# while loop so distance is constantly being checked
while(True):
    # call distance calculation
    distance = getDistance()
    # if distance is below a certain threshold execute rest of code
    if(distance <= 20):
        # capture webcam image
        ret, image = cam.read()

        # convert to in memory jpeg
        _, JPEG = cv2.imencode(".jpg", image, [int(cv2.IMWRITE_JPEG_QUALITY), 80])
        JPEG.tofile('DEBUG-original.jpg')

        # Base64 encode
        b64 = b64encode(JPEG)

        # JSON-encode
        message = { "image": b64.decode("utf-8") }
        messageJSON = json.dumps(message)

        # call iotcore to send image to aws as a json
        ImgDataService.setImg(messageJSON)

        # wait a second
        time.sleep(5)

        # get the response from iotcore
    else:
        continue




# calculating distance 
# GPIO.output(PIN_TRIGGER, GPIO.HIGH)

# time.sleep(0.00001)

# GPIO.output(PIN_TRIGGER, GPIO.LOW)

# GPIO.cleanup()




