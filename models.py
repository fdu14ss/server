import pymongo.errors
import flask.ext.login as flask_login
from app import app, db, Logger


class User(flask_login.UserMixin):
    def __init__(self, username):
        self.username = username
        self.id = username

    def add_doc(self, document):
        users = db.users
        users.findOne({'username': self.username})
        posts = db.posts
        post_id = posts.insert_one(document).inserted_id
        app.logger.debug(str(post_id))
        pass

    def edit_doc(self, document):
        pass

    @staticmethod
    def get(username):
        return User(username)

    @staticmethod
    def exist_in_db(username):
        try:
            app.logger.info('enter exist_in_db')
            users = db.users
            result = users.find_one({'username': username})
            if result:
                return True
            else:
                return False
        except pymongo.errors.PyMongoError as error:
            app.logger.log(error)
            return False

    @staticmethod
    def register(username, password):
        if User.exist_in_db(username):
            return {'status': False, 'cause': 'username already exists'}
        else:
            users = db.users
            users.insert_one({
                'username': username,
                'password': password
            })
            return {'status': True}

    @staticmethod
    def auth(username, password):
        if User.exist_in_db(username):
            users = db.users
            result = users.find_one({'username': username}, {'password':1, '_id': 0})
            Logger.debug(result['password'])
            if password != result['password']:
                return {'status': False, 'cause': 'wrong password'}
            else:
                return {'status': True}

        else:
            return {'status': False, 'cause': 'username does not exist'}

    def delete_doc(self, document):
        pass
