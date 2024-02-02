import os
import sys
from flask import Flask
from flask_cors import CORS
from datetime import datetime

if 'CURRENT_ENVIRONMENT' not in os.environ:
    print('===================================================================', file=sys.stderr)
    print('[ERROR] Missing value for CURRENT_ENVIRONMENT envrionment variable.', file=sys.stderr)
    print('[ERROR] Please specify it when you start the container.', file=sys.stderr)
    sys.exit(1)

# Create logs folder
log_dir = os.getenv('LOG_DIR', './logs')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

app = Flask(__name__)
CORS(app)

@app.route('/')
def default():
    return {
        "time": str(datetime.now()),
        "environment": os.environ['CURRENT_ENVIRONMENT'],
        "hostname": os.uname()[1],
        "result": "root"
    }    

@app.route("/get/<name>")
def get(name):
    return {
        "time": str(datetime.now()),
        "environment": os.environ['CURRENT_ENVIRONMENT'],
        "hostname": os.uname()[1],
        "result": name
    }

@app.route("/write/<something>")
def write(something):
    print(something)
    with open('logs/my-messages.log', 'a') as the_file:
        the_file.write(f"{something}\n")
    return {
        "status": "ok"
    }