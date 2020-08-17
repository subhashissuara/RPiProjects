import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

pinLED = 8
pinButton = 12

GPIO.setup(pinLED, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(pinButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        if (GPIO.input(pinButton) == 0):
            GPIO.output(pinLED, GPIO.HIGH)
        else:
            GPIO.output(pinLED, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pinLED, GPIO.LOW)
            time.sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()
