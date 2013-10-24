#coding : utf-8
from datetime import datetime
from flask import Flask, request, jsonify
from pymongo import MongoClient
import hashlib
from user import User


app = Flask(__name__)

client = MongoClient()
#Same as client = MongoClient('localhost', 27017)
#Or client = MongoClient('mongodb://localhost:27017/')

db = client.demo

@app.route('/')
def helloWorld():
    return 'Welome to the demo!'


@app.route("/user/<user_id>", methods=["GET", "PUT", "DELETE"])
def handleUser(user_id):
    app.logger.debug("Handling user")
    if request.method == "PUT":
        return "Put called on user with id "+user_id
    elif request.method == "DELTE":
        return "Delete called on user with id "+ user_id
    elif request.method == "GET":
        existingUser =  db.users.find_one({"_id": user_id})
        return existingUser.firstName

@app.route("/user", methods=["POST"])
def addUser():
    userName = request.form["username"]
    firstName = request.form["firstname"]
    lastName = request.form["lastname"]
    password = request.form["password"]
    created = datetime.now()

    user = User(userName=userName, firstName=firstName, lastName=lastName, password=password, created=created)
    id = db.users.insert(user.json())
    user._id = id
    return jsonify(user.json())



# @app.route("/message/<message_id", methods=["DELETE"])
# def deleteMessage():
#     pass
#
# @app.route("/message/<message_id", methods=["PUT"])
# def putMessage():
#     pass
#
# @app.route("/message", methods=["POST"])
# def postMessage():
#     pass


if __name__ == '__main__':
    app.run(debug=True)
