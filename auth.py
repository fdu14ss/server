"""
auth imports app and models, but none of those import auth
so we're OK
"""
import flask
import flask.ext.login as flask_login
from app import app, db, Logger
from models import User
Us

login_manager = flask_login.LoginManager()
login_manager.init_app(app)


@login_manager.user_loader  # reload the user from session
def user_loader(username):
    if not User.exist_in_db(username):
        Logger.debug('user does not exist in user_loader')
        return
    else:
        user = User.get(username)
        return user


# @login_manager.request_loader  # load the user from request
# def request_loader(request):
#     app.logger.debug('request_loader ' + request.method)
#     Logger.info('request_loader ' + request.method)
#     if request.method != 'POST':
#         app.logger.debug('this is a GET')
#         return
#     else:
#         app.logger.debug('could it be ....request_loader problem?')
#         Logger.info('could it be ....request_loader problem?')
#         req = request.form
#         username = req['username']
#         password = req['password']
#         # Logger.debug('user does not exist')
#         if not User.exist_in_db(username):
#             return
#         else:
#             user = User.get(username)
#             status = User.auth(username, password)['status']
#             Logger.debug('auth result= '+str(status))
#             if status == True:
#                 return user
#             else:
#                 return


@login_manager.unauthorized_handler
def unauthorized_handler():
    return flask.jsonify({'status': False,
                          'cause': 'unauthorized'})

