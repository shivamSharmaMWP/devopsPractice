from flask import Flask, request, render_template
import logging

from datetime import datetime


app = Flask(__name__)

# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='logging/example.log',level=logging.DEBUG)


def setup_logger(logger_name, log_file, level=logging.DEBUG):
    l = logging.getLogger(logger_name)
    #formatter = logging.Formatter('%(message)s')

    # hostname/container_id/datetime
    # comm_gateway_2020-07-30 16:12:28,286__Container_id_393829382938238938938938283238293829389

    formatter = logging.Formatter("%(asctime)s: %(levelname)s: %(message)s")

    
    fileHandler = logging.FileHandler(log_file, mode='w')
    fileHandler.setFormatter(formatter)
    
    
    streamHandler = logging.StreamHandler()
    streamHandler.setFormatter(formatter)

    l.setLevel(level)
    l.addHandler(fileHandler)
    l.addHandler(streamHandler)    


container_datetime = str(datetime.now()).replace(" ", "_")
import socket
container_id = socket.gethostname()
container_name = 'comm_gateway'

final_name = "logging/" + container_name + "_" + container_datetime +"_" + container_id + ".log"


setup_logger('log1', final_name)
# setup_logger('log2', txtName+"small.txt")
lg = logging.getLogger('log1')
# logger_2 = logging.getLogger('log2')



def create_app():
    print("creating app ")

    @app.route('/')
    def hello_world():
        lg.info('info log /')
        lg.debug('debug log / ')
        lg.error('error log /')
        lg.critical('critical log /')

        return 'Hello World!'

    @app.route('/first')
    def first():
        lg.critical('inside first /')
        return 'simple first'

if __name__ == '__main__':
    print("Configure App")
    create_app()

    app.run(debug=True, port=5084, host='0.0.0.0')
