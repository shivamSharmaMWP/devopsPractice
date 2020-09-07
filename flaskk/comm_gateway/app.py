from flask import Flask
import os
import socket

app = Flask(__name__)

@app.route("/")
def hello():

    return "version qa Flask inside Docker !!" + socket.gethostname()

@app.route("/send")
def hello_send():
    return "now sending."


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True,host='0.0.0.0',port=port)
