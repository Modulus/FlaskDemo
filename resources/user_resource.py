from datetime import datetime
import bcrypt
from flask.ext.restful import Resource, reqparse, marshal_with, abort
from mongoengine import DoesNotExist
from models.user import User

__author__ = 'john'


class UserResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("first_name", type=str, help="First name is required")
        self.parser.add_argument("last_name", type=str, help="Last name is required")
        self.parser.add_argument("user_name", type=str, help="User name is required")
        self.parser.add_argument("creation", type=datetime, help="Your creation")
        self.parser.add_argument("pass", type=str, help="Password is required")
        self.parser.add_argument("id", type=str, help="User id")
        self.args = self.parser.parse_args()

    @marshal_with(User.format())
    def post(self):

        firstName = self.args["first_name"]
        lastName = self.args["last_name"]
        userName = self.args["user_name"]
        passwd = self.args["pass"]


        hash = bcrypt.hashpw(passwd, bcrypt.gensalt())

        user = User(userName=userName, firstName=firstName, lastName=lastName, created=datetime.now(), password=hash)
        user.save()
        return user




    @marshal_with(User.format())
    def get(self, id):
        return User.objects.get(id=id)

    def put(self, user):
        User.save(user)
        return user

    def delete(self):
        id = self.args["id"]
        if not id:
            abort(500)
        else:
            existingUser = User.objects.get(id=id)
            existingUser.delete()