from flask import Flask
import logging
from logging import Formatter, FileHandler


app = Flask(__name__)
# TODO:change the secret_key
app.secret_key = 'super secret string'

Logger = logging.getLogger('whatever')
file_handler = FileHandler('logs/flask.log')
handler = logging.StreamHandler()
file_handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
handler.setFormatter(Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))
Logger.addHandler(file_handler)
Logger.addHandler(handler)
Logger.setLevel(logging.INFO)

from database import db





