#coding : utf-8
from datetime import datetime
import json
from bson import ObjectId
from flask import Flask, request, jsonify, make_response
from flask.ext.pymongo import PyMongo
from pymongo import MongoClient
import hashlib
from user import User


app = Flask(__name__)
app.config["MONGO_DBNAME"] = "demo"
mongo = PyMongo(app, config_prefix="MONGO")

#Same as client = MongoClient('localhost', 27017)
#Or client = MongoClient('mongodb://localhost:27017/')


@app.route('/')
def helloWorld():
    return 'Welome to the demo!'


@app.route("/user/<user_id>", methods=["GET", "PUT", "DELETE"])
def handleUser(user_id):
    app.logger.debug("Handling user")
    if request.method == "PUT":
        return "Put called on user with id "+user_id
    elif request.method == "DELTE":
        return "Delete called on user with id "+user_id
    elif request.method == "GET":
        existingUser = mongo.db.users.find_one({"_id": ObjectId(user_id)})
        existingUser["_id"] = str(existingUser["_id"])
        return jsonify(existingUser)

@app.route("/users", methods=["GET"])
def getAllUsers():
    users = []
    for user in mongo.db.users.find():
        app.logger.debug(user)
        user["_id"] = str(user["_id"])
        users.append(user)

    return jsonify(users=users)


@app.route("/user", methods=["POST"])
def addUser():
    userName = request.form["username"]
    firstName = request.form["firstname"]
    lastName = request.form["lastname"]
    password = request.form["password"]
    created = datetime.now()

    user = User(userName=userName, firstName=firstName, lastName=lastName, password=password, created=created)
    id = mongo.db.users.insert(user.json())
    user._id = id
    return jsonify(user.json())


@app.route("/messages/<user_id>/", methods=["GET"])
def getAllMesages(user_id):
    app.logger.debug("Fetching messages for user_id"+user_id)
    messages = []
    for message in mongo.db.messages.find({"sender": ObjectId(user_id)}):
        message["_id"] = str(message["_id"])
        message["sender"] = str(message["sender"])
        message["receiver"] = str(message["receiver"])
        messages.append(message)

    for message in mongo.db.messages.find({"receiver": ObjectId(user_id)}):
        message["_id"] = str(message["_id"])
        message["sender"] = str(message["sender"])
        message["receiver"] = str(message["receiver"])
        messages.append(message)

    return jsonify(results=messages)




@app.route("/message", methods=["POST"])
def postMessage():
    pass



# @app.route("/message/", methods=["DELETE"])
# def deleteMessage():
#     pass
#
# @app.route("/message/<message_id>", methods=["PUT"])
# def putMessage():
#     pass



if __name__ == '__main__':
    app.run(debug=True)
