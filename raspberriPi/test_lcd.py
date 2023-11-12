import Adafruit_CharLCD as LCD
from time import sleep

PIN_RS = 25
PIN_EN = 24
PIN_D4 = 23
PIN_D5 = 17
PIN_D6 = 16
PIN_D7 = 22
PIN_BACKLIGHT = 19


# Define LCD column and row size for 16x2 LCD.
PIN_COL = 16
PIN_ROW = 2

lcd = LCD.Adafruit_CharLCD(PIN_RS, PIN_EN, PIN_D4, PIN_D5, PIN_D6, PIN_D7, PIN_COL, PIN_ROW, PIN_BACKLIGHT)

lcd.message('Hello\nworld!')
sleep(5)
lcd.clear()
