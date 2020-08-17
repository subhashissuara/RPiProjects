import RPi.GPIO as GPIO 
import time

GPIO.setmode(GPIO.BOARD) # Use board pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and set initial value to low (off)

try:
    while True:
        GPIO.output(8, GPIO.HIGH) # Turn on
        time.sleep(1)
        GPIO.output(8, GPIO.LOW) # Turn off
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
