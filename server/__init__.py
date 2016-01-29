from flask import Flask


app = Flask(__name__)
# TODO:change the secret_key
app.secret_key = 'super secret string'

from server.database import db
import server.routes as routes




