from datetime import datetime
from pymongo import MongoClient
from models.message import Message
from models.user import User
import bcrypt

__author__ = 'john'


class Populator(object):
    def run(self):
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

        u1._id = db.users.insert(u1.json())
        u2._id = db.users.insert(u2.json())
        u3._id = db.users.insert(u3.json())
        u4._id = db.users.insert(u4.json())

        m1 = Message(
            sender=u1._id, subject="First message",
            message="This is the first ever message in the system?!",
            receiver=u4._id,
            sent=datetime.now()
        )

        m2 = Message(
            sender=u4._id, subject="RE: First message",
            message="It's awesome isn't it?",
            receiver=u1._id,
            sent=datetime.now()
        )

        m3 = Message(
            sender=u2._id, subject="Remember, remember",
            message="Remember to buy milk!!!!!!",
            receiver=u2._id,
            sent=datetime.now()
        )

        m4 = Message(
            sender=u3._id, subject="New project",
            message="We need an extra developer for a new ruby project, are you in?",
            receiver=u2._id,
            sent=datetime.now()
        )

        m5 = Message(
            sender=u2._id, subject="RE: New project",
            message="Sure why not, could we have a look at sinatra in that case?",
            receiver=u4._id,
            sent=datetime.now()
        )

        m1._id = db.messages.insert(m1.json())
        m2._id = db.messages.insert(m2.json())
        m3._id = db.messages.insert(m3.json())
        m4._id = db.messages.insert(m4.json())
        m5._id = db.messages.insert(m5.json())

if __name__ == "__main__":
    pop = Populator()
    pop.run()
