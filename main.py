import atexit
import config as pin_config
import RPi.GPIO as GPIO

from flask import Flask, jsonify, request

app = Flask(__name__)

## GPIO pin state machine
class Pins:
  def __init__(self):
    self.all = {}

  def set_all(self, pins):
    self.all = pins

pins = Pins()

pins.set_all(pin_config)

GPIO.setmode(GPIO.BCM)

## Go through pins and set them to out as default
def go_through_and_set_pins():
  for k, v in pins.all.items():
    GPIO.setup(int(k), GPIO.OUT)
    if bool(v):
      GPIO.output(int(k), GPIO.HIGH)
    else:
      GPIO.output(int(k), GPIO.LOW)

def merge_two_dicts(original, new):
  clone = original.copy()
  clone.update(new)
  return clone

## go through pins at bootup
go_through_and_set_pins()

@app.route("/")
def hello():
  return jsonify(pins.all)

@app.route("/pins", methods=["POST"])
def set_pins():
  payload = {}

  for k, v in request.get_json().items():
    if v == "false" or False:
      payload[int(k)] = False
    else:
      payload[int(k)] = True

  pins.set_all(
    merge_two_dicts(pins.all, payload)
  )

  go_through_and_set_pins()
  return jsonify(pins.all)

## Cleanup GPIO on exit
atexit.register(GPIO.cleanup)
