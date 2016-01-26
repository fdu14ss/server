from flask import Flask
from flask import request
import flask.ext.login as flask_login
import flask
import json

app = Flask(__name__)
# TODO:change the secret_key
app.secret_key = 'super secret string'

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

# our mock database
users = {'usr': {'pw': 'pw'}}


class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return
    else:
        user = User()
        user.id = email
        return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return
    else:
        user = User()
        user.id = email

        user.is_authenticated = request.form['pw'] == users[email]['pw']

        return user


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1>Home</h1>'


@app.route('/login', methods=['GET', 'POST'])
def login():
    # app.logger.debug('what the hell')
    if flask.request.method == 'GET':
        return '''
                   <form action='login' method='POST'>
                    <input type='text' name='email' id='email' placeholder='email'></input>
                    <input type='password' name='pw' id='pw' placeholder='password'></input>
                    <input type='submit' name='submit'></input>
                   </form>
                   '''

    email = flask.request.form['email']
    # app.logger.debug(email)
    # app.logger.debug(users[email])
    if request.form['pw'] == users[email]['pw']:
        user = User()
        user.id = email
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


if __name__ == '__main__':
    app.run(debug=True)
