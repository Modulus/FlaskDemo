#coding : utf-8
from datetime import datetime
from flask import Flask, request, jsonify
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
        existingUser = mongo.db.users.find_one({"_id": user_id})
        return existingUser

@app.route("/users", methods=["GET"])
def getAllUsers():
    users = []
    for user_dict in mongo.db.users.find():
        app.logger.debug(user_dict)
        user = User(
            firstName=user_dict["firstName"], lastName=user_dict["lastName"],
            userName=user_dict["userName"], password=user_dict["password"]
        )
        user._id = str(user_dict["_id"])
        user.created = user_dict["created"]
        users.append(user_dict)

    return users[1]


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
    return "User messages for user id: "+user_id


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
