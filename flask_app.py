import urlparse
from flask.ext.mongoengine import MongoEngine
import os
from resources.message_resource import MessageResource
from resources.users_resource import UsersResource

__author__ = 'modulus'
from flask import Flask
from flask.ext import restful
from resources.messages_resource import MessagesResource
from resources.user_resource import UserResource


class FlaskApp(object):

    def __init__(self):
        MONGOHQ_URL = os.environ.get('MONGOHQ_URL')

        self.app = Flask(__name__)

        self.app.config["MONGO_DBNAME"] = "demo"
        if MONGOHQ_URL:
            url = urlparse.urlparse(MONGOHQ_URL)
            self.app.config.setdefault('MONGODB_USERNAME', url.username)
            self.app.config.setdefault('MONGODB_PASSWORD', url.password)
            self.app.config.setdefault('MONGODB_HOST', url.hostname)
            self.app.config.setdefault('MONGODB_PORT', url.port)
            self.app.config.setdefault('MONGODB_DB', url.path[1:])

        else:
            self.app.config["MONGODB_HOST"] = "localhost"
            self.app.config["MONGODB_PORT"] = "27017"
            self.app.config["MONGODB_DB"] = "demo"

        self.db = MongoEngine(self.app)

        self.api = restful.Api(self.app)
        self.api.add_resource(UserResource, "/user/<string:id>", "/user", "/user/")
        self.api.add_resource(UsersResource, "/", "/users", "/user/<string:user_id>/friends",
                              "/user/<string:user_id>/friends/")
        self.api.add_resource(MessageResource, "/message/<string:message_id>", "/message/<string:message_id>/")
        self.api.add_resource(MessagesResource, "/messages/<string:user_id>", "/messages/<string:user_id>/")

    def run(self, debug=False):
        self.app.run(debug=debug)


if __name__ == "__main__":
    app = FlaskApp()
    app.run(True)
