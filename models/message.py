from datetime import datetime

__author__ = 'john'


class Message(object):
    def __init__(self, **kwargs):
        self.sender = kwargs["sender"]
        self.subject = kwargs["subject"]
        self.message = kwargs["message"]
        self.receiver = kwargs["receiver"]
        self.sent = kwargs["sent"]
        self.read = False

    def json(self):
        return \
            {
                "sender": self.sender,
                "receiver": self.receiver,
                "subject": self.subject,
                "message": self.message,
                "sent": self.sent,
                "read": self.read
            }