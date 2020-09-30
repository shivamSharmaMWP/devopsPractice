
from flask import Flask
import os
import socket
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return {
        "value": "its first service " + socket.gethostname()
    }

fullname = os.getenv("FULLNAME")
# namespace = os.getenv("namespace", "")
# worker_host = "worker" + namespace

@app.route("/backend")
def backend():
    r = requests.get(fullname)
    # r = requests.get("http://"+worker_host + ":5001")
    # worker = socket.gethostbyname(worker_host)
    # return "Worker Message: {}\nFrom: {}".format(r.content, worker)

    return "Worker Message: {}\n".format(r.content)


# @app.route("/send-me")
# def hello_send_me():
#     r = requests.get(url="http://comm:5000")
#     client = r.json()
#     print("##### sender details {}".format(str(client)))
#     return "now sending.##### sender details {}".format(str(client))

# @app.route("/send-them")
# def hello_send_them():
#     r = requests.get(url="http://comm_2:5001")
#     print("##### sender details {}".format(str(r)))
#     client = r.json()
#     print("##### sender details {}".format(str(client)))
#     return "now sending.##### sender details {}".format(str(client))


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
