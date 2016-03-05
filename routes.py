import os

import functools
import flask

from werkzeug.utils import secure_filename

from app import app,Logger
from auth import flask_login
from models import User

from flask import request, jsonify, g


ALLOWED_EXTENSIONS = {'png', 'jpg', 'txt','html', 'css', 'js'}
UPLOAD_FOLDER = 'projects'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.before_request
def before_request():
    g.user = flask_login.current_user


def print_current_user():
    app.logger.info('current user: ' + flask_login.current_user.id)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def post_only(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if request.method == 'GET':
            return jsonify({'status': False, 'cause': 'only POST is supported'})
        else:
            return func(*args, **kwargs)

    return wrapper


def before_login_only(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if g.user is not None and g.user.is_authenticated:
            return jsonify({'status': False, 'cause': 'already logged in'})
        else:
            return func(*args, **kwargs)

    return wrapper


############################ routes ################################


@app.route('/', methods=['GET', 'POST'])
# @post_only
def home():
    return '''
    <!doctype html>
    <title>Clover</title>
    <h1>Homepage For the Clover Project</h1>
    <p>Enjoy it with given APIs!</p>
    '''

# 注册


@app.route('/register', methods=['GET', 'POST'])
@post_only
@before_login_only
def register():
    # if request.method == 'GET':
    #     return  '''
    # <!doctype html>
    # <title>User Register</title>
    # <h1>register</h1>
    # <form action="" method=post enctype=multipart/form-data>
    #   <p><input type=text name=username>
    #     <input type=password name=password>
    #      <input type=submit value=register>
    # </form>
    # '''

    username = request.json['username']
    password = request.json['password']
    return jsonify(User.register(username, password))


# 登入/登出
@app.route('/login', methods=['GET', 'POST'])
@post_only
@before_login_only
def login():
    #
    #
    # if request.method == 'GET':
    #     # if g.user is not None and g.user.is_authenticated:
    #         # return jsonify({'status': False, 'cause': 'already logged in'})
    #     Logger.info('login GET')
    #     return jsonify({'status': False, 'cause': 'only POST is allowed'})
    #     # return  '''
    #     # <!doctype html>
    #     # <title>Login</title>
    #     # <h1>login</h1>
    #     # <form action="" method=post enctype=multipart/form-data>
    #     #   <p><input type=text name=username>
    #     #     <input type=password name=password>
    #     #      <input type=submit value=login>
    #     # </form>
    #     # '''

    username = request.json['username']
    password = request.json['password']
    Logger.info('login POST')

    auth_result = User.auth(username, password)
    if auth_result['status']:
        Logger.debug('before login_user')
        user = User.get(username)
        flask_login.login_user(user)
        Logger.debug('after login_user')
        return flask.jsonify({'status': True})
    else:
        return flask.jsonify(auth_result)


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


@app.route('/users/<username>/projects/', methods=['GET', 'POST'])
@flask_login.login_required
def upload_project(username):
    if flask.request.method == 'GET':
        return  '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

    else:
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return jsonify({'status': True})
        else:
            return jsonify({'status': False})


@app.route('/after_login', methods=['GET'])
@flask_login.login_required
def after_login():
    return '<h1>You\'ve logged in<h1>'
