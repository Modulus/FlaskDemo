from datetime import datetime
import os
from pymongo import MongoClient
from models.message import Message
from models.user import User
import bcrypt

__author__ = 'john'


class Populator(object):
    def run(self):

        MONGO_URL = os.environ.get('MONGOHQ_URL')
        if MONGO_URL:
            client = MongoClient(MONGO_URL)
        else:
            client = MongoClient()
        db = client.demo
        db.users.drop()
        db.messages.drop()

        u1 = User(firstName="John", lastName="Doe", userName="John1",
                  password=bcrypt.hashpw("1234password", bcrypt.gensalt()))
        u1.created = datetime.now()

        u2 = User(firstName="Jane", lastName="Doe", userName="Jane",
                  password=bcrypt.hashpw("mypassw0rd", bcrypt.gensalt()))
        u2.created = datetime.now()

        u3 = User(firstName="Kristel", lastName="Nielsen", userName="Kristel",
                  password=bcrypt.hashpw("asdfda3", bcrypt.gensalt()))
        u3.created = datetime.now()

        u4 = User(firstName="Erik", lastName="Johannesen", userName="Erik",
                  password=bcrypt.hashpw("kjasdfj8i32", bcrypt.gensalt()))
        u4.created = datetime.now()

        u1.save()
        u2.save()
        u3.save()
        u4.save()

        m1 = Message(
            sender=u1.id, subject="First message",
            message="This is the first ever message in the system?!",
            receiver=u4.id,
            sent=datetime.now()
        )

        m2 = Message(
            sender=u4.id, subject="RE: First message",
            message="It's awesome isn't it?",
            receiver=u1.id,
            sent=datetime.now()
        )

        m3 = Message(
            sender=u2.id, subject="Remember, remember",
            message="Remember to buy milk!!!!!!",
            receiver=u2.id,
            sent=datetime.now()
        )

        m4 = Message(
            sender=u3.id, subject="New project",
            message="We need an extra developer for a new ruby project, are you in?",
            receiver=u2.id,
            sent=datetime.now()
        )

        m5 = Message(
            sender=u2.id, subject="RE: New project",
            message="Sure why not, could we have a look at sinatra in that case?",
            receiver=u4.id,
            sent=datetime.now()
        )

        m1.save()
        m2.save()
        m3.save()
        m4.save()
        m5.save()

if __name__ == "__main__":
    pop = Populator()
    pop.run()
