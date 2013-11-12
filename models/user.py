from datetime import datetime
from flask.ext.restful import fields
from mongoengine import StringField
from mongoengine.fields import DateTimeField

__author__ = 'john'


class User(object):

    firstName = StringField()
    lastName = StringField()
    userName = StringField()
    password = StringField()
    created = DateTimeField(required=True, default=datetime.now)

    @staticmethod
    def format():
        return {
            "firstName": fields.String,
            "lastName": fields.String,
            "userName": fields.String,
            "password": fields.String,
            "created": fields.DateTime
        }


