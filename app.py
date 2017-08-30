#!flask/bin/python
import requests
import os
import sys
import logging
import datetime
import time

from flask import Flask, request
from flask_prometheus import monitor

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.DEBUG)

@app.route('/')
def index():
    # Call Greeter Service
    timestamp = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    app.logger.debug("Starting at: " + timestamp)

    # Check if a sleep was passed in as a parameter
    sleep = request.args.get("sleep")
    if sleep is not None:
      app.logger.debug("Sleeping for " + sleep + " seconds")
      time.sleep(int(sleep))
    else:
      # Force a sleep.
      # Comment this for demo purposes
      app.logger.debug("Forcing a sleep")
 #     time.sleep(2)

    timestamp2 = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    app.logger.debug("Finished at: " + timestamp2)
    return timestamp2 + " Hello, World! - v2\n"

if __name__ == '__main__':
    monitor(app, port=8000)
    app.run(host='0.0.0.0')
