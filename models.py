
import flask.ext.login as flask_login
from app import app, db

users = {'wjt': {'pw': 'pw'}}


class User(flask_login.UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = username

    def add_doc(self, document):
        posts = db.posts
        post_id = posts.insert_one(document).inserted_id
        app.logger.debug(str(post_id))
        pass

    def edit_doc(self, document):
        pass

    @staticmethod
    def get(username):
        return User(username)

    def delete_doc(self, document):
        pass