# PiPyIO

Python API for GPIO on the Raspberry Pi!

```bash
pip3 install flask
```

Run the API server: `./start.sh`

To turn on pin 17: `curl -d '{ "17": "true" }' -H "Content-Type: application/json" -X POST localhost:9001/pins`

To turn off pin 17: `curl -d '{ "17": "false" }' -H "Content-Type: application/json" -X POST localhost:9001/pins`

Stopping the server with `^C` or any kind of SIGKILL will reset GPIO state.
