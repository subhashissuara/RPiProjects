import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pinButton = 12

GPIO.setup(pinButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        print(GPIO.input(pinButton))
        time.sleep(1)
        
except KeyboardInterrupt:
    GPIO.cleanup()
