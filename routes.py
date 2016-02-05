import functools
import flask

from app import app
from auth import flask_login
from models import User, users


def print_current_user():
    app.logger.debug('current user: ' + flask_login.current_user.id)


def post_only(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if flask.request.method == 'GET':
            return flask.jsonify({'status': False, 'cause': 'only POST is supported'})
        else:
            app.logger.debug(args)
            return func(*args, **kwargs)

    return wrapper


@app.route('/', methods=['GET', 'POST'])
# @post_only
def home():
    return '<h1>Home</h1>'


# 登入/登出
@app.route('/login', methods=['GET', 'POST'])
@post_only
def login():
    req = flask.request.get_json()
    username = req['username']
    if req['pw'] == users[username]['pw']:
        user = User.get(username)
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


@app.route('/users/<username>/projects/<int:project_id>', methods=['GET'])
@flask_login.login_required
def get_static(username, project_id):
    # print_current_user()
    if flask_login.current_user.id == username:
        return flask.send_from_directory('projects', str(project_id)+'.png')

