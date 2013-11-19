__author__ = 'Modulus'
from flask.ext.restful import Resource, marshal_with
from ..models.message import Message


class MessagesResource(Resource):


    @marshal_with(Message.format())
    def get(self):
        return list(Message.objects.all())
