# PiPyIO

Python API for GPIO on the Raspberry Pi!

1. `pip3 install flask`
1. Run the API server: `./scripts/start.sh`

Once you have installed Flask, no need to do it again :tada:

### The API

To turn **on** pin 17 (default pin in config):

`curl -d '{ "17": "true" }' -H "Content-Type: application/json" -X POST localhost:9001/pins`

To turn **off** pin 17 (default pin in config):

`curl -d '{ "17": "false" }' -H "Content-Type: application/json" -X POST localhost:9001/pins`

Stopping the server with `^C` (control + c) will reset (wipe) GPIO state.

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

Note that you do not need to initialize with all intended pins. Adding a new pin via a POST request will automatically update internal state for the API.

### Running in the background

`sudo apt install screen -y`

Then:

`./scripts/bg.sh`

If you need to shut the server down, simply call the shutdown script: `./scripts/shutdown.sh`

***

Happy Hacking! :smile:
