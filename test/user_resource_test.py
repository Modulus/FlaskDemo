from unittest import TestCase
from flask.ext.mongoengine import MongoEngine
from mongoengine import connect
from flask_app_new import app
from flask_app_new import initApi, initDb
from models.user import User

__author__ = 'modulus'




class UserResouceTest(TestCase):

    app.config.setdefault("MONGODB_DB", "demo_test")
    app.config["MONGODB_DB"] = "demo_test"
    app.config["MONGODB_HOST"] = "locahost"
    # app.config["MONGODB_PORT"] = "28017
    app.config["DEBUG"] = True

    connect(app.config["MONGODB_DB"])
    initDb()
    initApi()

# app.config.from_object("settings")
    # @classmethod
    # def tearDownClass(cls):
    #     User.drop_collection()


    def testDB(self):
        self.assertEquals("demo_test", app.config["MONGODB_DB"])

    def test_post_user(self):



        client = app.test_client()

        result = client.post("/user", data={"id": None, "first_name": "John", "last_name": "Skauge", "user_name": "John", "pass": "MyPassword"})
        self.assertTrue(result.data["id"])
        self.assertEquals("John", result.data["firstName"])
        self.assertEquals("Skauge", result.data["lastName"])
        self.assertEquals("John", result.data["userName"])



