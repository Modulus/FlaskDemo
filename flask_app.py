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

MONGOHQ_URL = os.environ.get('MONGOHQ_URL')

app = Flask(__name__)


def createApp(configFileName):

    app.config.from_object(configFileName)

    db = MongoEngine(app)

    db.init_app(app)

    api = restful.Api(app)
    api.add_resource(UserResource, "/user/<string:id>", "/user", "/user/")
    api.add_resource(UsersResource, "/", "/users", "/user/<string:user_id>/friends",
                     "/user/<string:user_id>/friends/")
    api.add_resource(MessageResource, "/message/<string:message_id>", "/message/<string:message_id>/")
    api.add_resource(MessagesResource, "/messages/<string:user_id>", "/messages/<string:user_id>/")

    return app

if __name__ == "__main__":
    app = createApp("settings")
    app.run(debug=True)


