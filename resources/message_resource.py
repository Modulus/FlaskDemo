__author__ = 'Modulus'
from flask.ext.restful import Resource, marshal_with, reqparse, abort

from models.message import Message


class MessageResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("id", type=str, help="Message id")
        self.parser.add_argument("text", type=str, help="Message text")
        self.parser.add_argument("receiver", type=str, help="Receiver of this message")
        self.parser.add_argument("sender", type=str, help="Sender of this message")

    @marshal_with(Message.format())
    def get(self, id):
        return Message.objects.get(id=id)

    def put(self):
        pass

    def post(self):
        pass

    def delete(self):
        m_id = self.args["id"]
        if not id:
            abort(500)
        else:
            message = Message.objects.get(id=m_id)
            message.delete()


