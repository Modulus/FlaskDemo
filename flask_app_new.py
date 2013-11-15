from resources.message_resource import MessageResource
from resources.users_resource import UsersResource

__author__ = 'modulus'
from flask import Flask, url_for, render_template
from flask.ext import restful
# from resources.user_list_resource import ImageResource
from resources.messages_resource import MessagesResource
from resources.user_resource import UserResource


class FlaskApp(object):

    def __init__(self):
        self.app = Flask(__name__)
        self.api = restful.Api(self.app)
        self.api.add_resource(UserResource, "/user/<string:id>", "/user", "/user/")
        self.api.add_resource(UsersResource, "/users", "/user/<string:user_id>/friends",
                                             "/user/<string:user_id>/friends/")
        self.api.add_resource(MessageResource, "/message/<string:message_id>", "/message/<string:message_id>/")
        self.api.add_resource(MessagesResource, "/messages/<string:user_id>", "/messages/<string:user_id>/")
