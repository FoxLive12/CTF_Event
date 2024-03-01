from flask import *
from configuration import Configuration

app = Flask(__name__, static_folder='static')

app.config.from_object(Configuration)