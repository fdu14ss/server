

from flask import request
import flask.ext.login as flask_login
import flask
from server import app
from server.models import User
from server.models import users
# our mock database


login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return
    else:
        user = User.get(email)
        return user


@login_manager.request_loader
def request_loader(request):
    req = request.get_json()
    email = req['email']
    if email not in users:
        return
    else:
        user = User.get(email)
        user.is_authenticated = req['pw'] == users[email]['pw']
        return user


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    # app.logger.debug('what the hell')
    if flask.request.method == 'GET':
        return

    req = flask.request.get_json()
    email = req['email']
    # app.logger.debug(email)
    # app.logger.debug(users[email])
    if req['pw'] == users[email]['pw']:
        user = User.get(email)
        # app.logger.debug(user.get_id())
        flask_login.login_user(user)
        app.logger.debug('current user: ' + flask_login.current_user.id)
        return flask.redirect(flask.url_for('after'))
    else:
        return 'Bad login'


@app.route('/after')
@flask_login.login_required
def after():
    app.logger.debug('enter here')
    return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout')
def logout():
    flask_login.logout_user()
    return 'Logged out'


@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'

