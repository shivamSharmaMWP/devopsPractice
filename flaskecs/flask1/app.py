
from flask import Flask
import os
import socket
import requests

import logging
import time
import redis

logger = logging.getLogger("simple")

app = Flask(__name__)

@app.route("/")
def hello():
    return {
        "value": "its first service " + socket.gethostname()
    }

@app.route("/flask1")
def helloflask1():
    return {
        "value": "its first service " + socket.gethostname()
    }


@app.route("/flask2")
def backend():
    flask2Url = os.getenv("FLASK_2_URL")
    logger.info('url captured is ' + flask2Url)
    # namespace = os.getenv("namespace", "")
    # worker_host = "worker" + namespace

    r = requests.get(flask2Url)
    # r = requests.get("http://"+worker_host + ":5001")
    # worker = socket.gethostbyname(worker_host)
    # return "Worker Message: {}\nFrom: {}".format(r.content, worker)

    return "Worker Message: {}\n".format(r.content)


cache = redis.Redis(os.getenv('REDIS'), port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/redis')
def helloredis():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)






if __name__ == "__main__":

    app.run(debug=True,host='0.0.0.0',port=5000)
