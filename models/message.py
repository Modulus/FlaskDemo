from datetime import datetime
from flask.ext.restful import fields
from mongoengine import Document, ReferenceField, StringField, DateTimeField, BooleanField
from models.user import User

__author__ = 'john'


class Message(Document):

    sender = ReferenceField(User)
    subject = StringField()
    text = StringField()
    receiver = ReferenceField(User)
    sent = DateTimeField(required=True, default=datetime.now)
    read = BooleanField(default=False)

    meta = {
        "collection": "messages"
    }

    @staticmethod
    def format():
        return {
            "sender": fields.Nested(Message.userFormat()),
            "subject": fields.String,
            "text": fields.String,
            "sent": fields.DateTime,
            "receiver": fields.Nested(Message.userFormat()),
            "read": fields.Boolean
        }

    @staticmethod
    def userFormat():
        return {
            "userName": fields.String
        }
