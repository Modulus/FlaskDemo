from datetime import datetime
from flask.ext.restful import fields
from mongoengine import StringField, Document
from mongoengine.fields import DateTimeField

__author__ = 'john'


class User(Document):

    firstName = StringField()
    lastName = StringField()
    userName = StringField()
    password = StringField()
    created = DateTimeField(required=True, default=datetime.now)

    meta = {
        "collection": "users"
    }

    @staticmethod
    def format():
        return {
            "firstName": fields.String,
            "lastName": fields.String,
            "userName": fields.String,
            "password": fields.String,
            "created": fields.DateTime
        }


