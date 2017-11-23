# PiPyIO

Python API for GPIO on the Raspberry Pi!

```bash
pip3 install flask
```

Run the API server: `./start.sh`

To turn on pin 17:

`curl -d '{ "17": "true" }' -H "Content-Type: application/json" -X POST localhost:9001/pins`

To turn off pin 17:

`curl -d '{ "17": "false" }' -H "Content-Type: application/json" -X POST localhost:9001/pins`

Stopping the server with `^C` or any kind of SIGKILL will reset GPIO state.

### Initial Pin State

On bootup you can dictate which **BCM Pin #** will be _on or off_ by modifying the config class.

This file is located in: [`lib/config.py`](https://github.com/selfup/pipyio/blob/master/lib/config.py)

Inside of the `__init__` method, there is a `self.pins` dictionary:

```python
self.pins = {
  17: True,
}
```

That is the object/dictionary to modify.

`True` means **on**, `False` would mean **off**.

You can add pins as you please, just realize that the API is not meant for PWM or any fancy pins yet. So far these are just basic _on / off_ pins.

Example modified dictionary:

```python
self.pins = {
  17: False,
  27: False,
  22: True,
}
```