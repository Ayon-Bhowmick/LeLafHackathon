import Adafruit_CharLCD as LCD
from time import sleep

PIN_RS = 8
PIN_EN = 15
PIN_D4 = 13
PIN_D5 = 7
PIN_D6 = 5
PIN_D7 = 3
PIN_BACKLIGHT = 2


# Define LCD column and row size for 16x2 LCD.
PIN_COL = 16
PIN_ROW = 2

lcd = LCD.Adafruit_CharLCD(PIN_RS, PIN_EN, PIN_D4, PIN_D5, PIN_D6, PIN_D7, PIN_COL, PIN_ROW, PIN_BACKLIGHT)

lcd.message("Hi\n")
