import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BOARD) # Use board pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

while True:
    GPIO.output(8, GPIO.HIGH) # Turn on
    sleep(1)
    GPIO.output(8, GPIO.LOW) # Turn off
    sleep(1)