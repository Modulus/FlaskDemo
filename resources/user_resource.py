from datetime import datetime
import bcrypt
from flask.ext.restful import Resource, reqparse, marshal_with
from models.user import User

__author__ = 'john'


class UserResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("first_name", type=str, help="First name is required")
        self.parser.add_argument("last_name", type=str, help="Last name is required")
        self.parser.add_argument("user_name", type=str, help="User name is required")
        self.parser.add_argument("birth_date", type=datetime, help="Your birthday")
        self.parser.add_argument("pass", type=str, help="Password is required")
        self.parser.add_argument("id", type=str, help="User id")
        self.args = self.parser.parse_args()

    @marshal_with(User.format())
    def post(self):

        firstName = self.args["first_name"]
        lastName = self.args["last_name"]
        userName = self.args["user_name"]
        created = datetime.now()
        passwd = self.args["pass"]
        created = datetime.now()
        hash = bcrypt.hashpw(passwd, bcrypt.gensalt())

        user = User(userName=userName, firstName=firstName, lastName=lastName, created=created, password=passwd)
        user.save()

        return user