
import flask

from app import app
from auth import flask_login
from models import User, users


def print_current_user():
    app.logger.debug('current user: ' + flask_login.current_user.id)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


# 登入/登出


@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        return flask.jsonify({'status': False, 'cause': 'only POST is supported'})
    else:
        req = flask.request.get_json()
        email = req['email']
        if req['pw'] == users[email]['pw']:
            user = User.get(email)
            flask_login.login_user(user)
            # return flask.redirect(flask.url_for('after'))
            return flask.jsonify({'status': True})
        else:
            return flask.jsonify({'status': False, 'cause': 'username or password is wrong'})


# @app.route('/after', methods=['GET', 'POST'])
# @flask_login.login_required
# def after():
#     return 'Logged in as: ' + flask_login.current_user.id


@app.route('/logout', methods=['GET'])
@flask_login.login_required
def logout():
    flask_login.logout_user()
    return flask.jsonify({'status': True})




