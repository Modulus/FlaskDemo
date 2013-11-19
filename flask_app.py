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

if MONGOHQ_URL:
    url = urlparse.urlparse(MONGOHQ_URL)
    app.config.setdefault("MONGODB_USERNAME", url.username)
    app.config.setdefault("MONGODB_PASSWORD", url.password)
    app.config.setdefault("MONGODB_HOST", url.hostname)
    app.config.setdefault("MONGODB_PORT", url.port)
    app.config.setdefault("MONGODB_DB", url.path[1:])
else:
    # app.config["MONGO_DBNAME"] = "demo"
    app.config.setdefault("MONGODB_HOST",  "localhost")
    app.config.setdefault("MONGODB_PORT",  "27017")
    app.config.setdefault("MONGODB_DB", "demo")

def initDb():
    return MongoEngine(app)

def initApi():
    api = restful.Api(app)
    api.add_resource(UserResource, "/user/<string:id>", "/user", "/user/")
    api.add_resource(UsersResource, "/", "/users", "/user/<string:user_id>/friends",
                     "/user/<string:user_id>/friends/")
    api.add_resource(MessageResource, "/message/<string:message_id>", "/message/<string:message_id>/")
    api.add_resource(MessagesResource, "/messages/<string:user_id>", "/messages/<string:user_id>/")

    return api

if __name__ == "__main__":
    db = initDb()
    api = initApi()
    app.run(debug=True)

