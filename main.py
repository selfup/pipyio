from flask import Flask, jsonify, request

from lib.config import Config
from lib.pins import Pins
from lib.gpio import Gpio

app = Flask(__name__)
pins = Pins()
gpio = Gpio()
config = Config()

pins.update(config.pins)
gpio.set_pins(pins)

@app.route("/")
def root():
  return jsonify(pins.all)

@app.route("/pins", methods=["POST"])
def set_pins():
  payload = {}

  for k, v in request.get_json().items():
    if v == "false" or False:
      payload[int(k)] = False
    else:
      payload[int(k)] = True

  pins.update(payload)
  gpio.set_pins(pins)

  return jsonify(pins.all)
