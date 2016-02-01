"""
auth imports app and models, but none of those import auth
so we're OK
"""
import flask
import flask.ext.login as flask_login
from app import app, db
from models import User, users


login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader  # reload the user from session
def user_loader(email):
    if email not in users:
        return
    else:
        user = User.get(email)
        return user


@login_manager.request_loader  # load the user from request
def request_loader(request):
    app.logger.debug(request.method)
    if request.method != 'POST':
        return
    else:
        req = request.get_json()
        email = req['email']
        if email not in users:
            return 'shit'
        else:
            user = User.get(email)
            user.is_authenticated = req['pw'] == users[email]['pw']
            return user


@login_manager.unauthorized_handler
def unauthorized_handler():
    return flask.jsonify({'status': False,
                          'cause': 'unauthorized'})

