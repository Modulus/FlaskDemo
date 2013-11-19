from datetime import datetime
import bcrypt
from flask.ext.restful import Resource, reqparse, marshal_with, abort
from mongoengine import DoesNotExist, ValidationError
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


        passHash = bcrypt.hashpw(passwd, bcrypt.gensalt())

        user = User(userName=userName, firstName=firstName, lastName=lastName, created=datetime.now(), password=passHash)
        user.save()
        return user




    @marshal_with(User.format())
    def get(self):
        try:
            user_id = self.args["id"]
            return User.objects.get(id=user_id)
        except DoesNotExist:
            return None
        except ValidationError:
            return None

    def put(self, user):
        User.save(user)
        return user

    def delete(self):
        user_id = self.args["id"]
        if not id:
            abort(500)
        else:
            try:
                existingUser = User.objects.get(id=user_id)
                existingUser.delete()
                return 200
            except DoesNotExist:
                abort(500)
            except ValidationError:
                abort(500)