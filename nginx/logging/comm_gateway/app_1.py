from flask import Flask, request, render_template
import logging


app = Flask(__name__)

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log',level=logging.DEBUG)

def create_app():
    print("creating app ")

    @app.route('/')
    def hello_world():
        logging.info('info log /')
        logging.debug('debug log / ')
        logging.error('error log /')
        logging.critical('critical log /')

        return 'Hello World!'

    @app.route('/first')
    def first():
        return 'simple first'

if __name__ == '__main__':
    print("Configure App")
    create_app()

    app.run(debug=True, port=5084, host='0.0.0.0')
