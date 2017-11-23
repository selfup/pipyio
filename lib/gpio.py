import atexit
import RPi.GPIO as GPIO

class Gpio:
  def __init__(self):
    GPIO.setmode(GPIO.BCM)
    atexit.register(GPIO.cleanup)

  def set_pins(self, pins):
    for k, v in pins.all.items():
      GPIO.setup(int(k), GPIO.OUT)
      if bool(v):
        GPIO.output(int(k), GPIO.HIGH)
      else:
        GPIO.output(int(k), GPIO.LOW)
