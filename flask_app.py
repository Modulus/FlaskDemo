#coding : utf-8
from datetime import datetime
import os
import logging
import sys
from bson import ObjectId
from flask import Flask, request, jsonify
from flask.ext.pymongo import PyMongo
from models.message import Message
import bcrypt
from models.user import User

#MongoHQ url on heroku
MONGO_URL = os.environ.get('MONGOHQ_URL')

app = Flask(__name__)
app.config["MONGO_DBNAME"] = "demo"
if MONGO_URL:
    app.config["MONGO_URI"] = MONGO_URL

    #Configure logger for heroku

    logging.basicConfig(stream=sys.stdout, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                        level=logging.DEBUG)

mongo = PyMongo(app, config_prefix="MONGO")

#Same as client = MongoClient('localhost', 27017)
#Or client = MongoClient('mongodb://localhost:27017/')

@app.route('/')
def helloWorld():
    return jsonify({"header": "Welcome to the demo!", "message":
                    "This will show simple usage of Python Flask and Pymongo"})


@app.route("/user/<user_id>", methods=["GET", "PUT", "DELETE"])
def handleUser(user_id):
    app.logger.debug("Handling user")

    if request.method == "PUT":
        return "Put called on user with id "+user_id

    elif request.method == "DELETE":
        user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if user is not None:
            app.logger.debug("Delete called on user with id [{userid}]".format(userid=user["_id"]))
            mongo.db.users.remove({"_id": ObjectId(user["_id"])})
            user["_id"] = str(user["_id"])
            return jsonify(user)
        else:
            return jsonify({"Message": "Non existing user"})

    elif request.method == "GET":
        existingUser = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        if existingUser is not None:
            existingUser["_id"] = str(existingUser["_id"])
            return jsonify(existingUser)
        else:
            return jsonify({"Message": "Non existing user"})

@app.route("/users", methods=["GET"])
def getAllUsers():
    users = []
    logger = logging.getLogger("UserLogger")
    logger.debug("Getting users")
    for user in mongo.db.users.find():
        logger.debug(user)
        user["_id"] = str(user["_id"])
        users.append(user)

    return jsonify(users=users)


@app.route("/user", methods=["POST"])
def addUser():
    logger = logging.getLogger()
    logger.debug("Adding user")
    userName = request.form["username"]
    firstName = request.form["firstname"]
    lastName = request.form["lastname"]
    password = request.form["password"]
    created = datetime.now()
    hash = bcrypt.hashpw(password, bcrypt.gensalt())

    existingUser = mongo.db.users.find({"userName": userName})

    if existingUser is None:
        user = User(userName=userName, firstName=firstName, lastName=lastName, password=hash, created=created)
        id = mongo.db.users.insert(user.json())
        user._id = id
        return jsonify(user.json())
    else:
        return jsonify({"message"  "User allready exists"})


@app.route("/user/<user_id>/messages", methods=["GET"])
def getAllMessages(user_id):
    app.logger.debug("Fetching messages for user_id"+user_id)
    messages = []

    #Compact way of query
    for message in mongo.db.messages.find({"$or": [{"sender": ObjectId(user_id)}, {"receiver": ObjectId(user_id)}]}):
        message["_id"] = str(message["_id"])
        message["sender"] = str(message["sender"])
        message["receiver"] = str(message["receiver"])
        messages.append(message)

    return jsonify(results=messages)

@app.route("/user/<user_id>/message/<message_id>", methods=["GET"])
def getMessage(user_id, message_id):
    message = mongo.db.messages.find_one({"$and" : [{"sender": ObjectId(user_id)}, {"_id": ObjectId(message_id)}] })

    message["_id"] = str(message["_id"])
    message["sender"] = str(message["sender"])
    message["receiver"] = str(message["receiver"])

    return jsonify(message)


@app.route("/message", methods=["POST"])
def postMessage():
    senderId = request.form["senderid"]
    receiverId = request.form["receiverid"]
    subject = request.form["subject"]
    text = request.form["text"]

    message = Message(sender=senderId, receiver=receiverId, subject=subject, message=text, sent=datetime.now())

    return jsonify(message)

# @app.route("/message/", methods=["DELETE"])
# def deleteMessage():
#     pass
#
@app.route("/user/<user_id>/message/<message_id>", methods=["PUT"])
def putMessage(user_id, message_id):
    message = request.form["message"]
    senderId = request.form["senderid"]



if __name__ == '__main__':
    app.run(debug=True)
