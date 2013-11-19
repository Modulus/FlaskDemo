import unittest

__author__ = 'modulus'

import json
from unittest import TestCase
from mongoengine import connect, DoesNotExist
from flask_app import initApi, initDb, app
from models.user import User




class UserResouceTest(TestCase):

    app.config.setdefault("MONGODB_DB", "demo_test")
    app.config["MONGODB_DB"] = "demo_test"
    app.config["MONGODB_HOST"] = "locahost"
    app.config["MONGODB_PORT"] = "27017"
    app.config["DEBUG"] = True
    headers = [('Content-Type', 'application/json')]

    connect(app.config["MONGODB_DB"])
    initDb()
    initApi()
    client = app.test_client()

    @classmethod
    def tearDownClass(cls):
        User.drop_collection()

    def testDB(self):
        self.assertEquals("demo_test", app.config["MONGODB_DB"])

    def testPostUser(self):

        result = self.client.post("/user", data={"first_name": "John", "last_name": "Skauge", "user_name": "John", "pass": "MyPassword"})

        userDict = json.loads(result.data)
        #Id should not leak out, this user dict is used in the ui
        self.assertTrue(userDict["id"])
        self.assertEquals("John", userDict["firstName"])
        self.assertEquals("Skauge", userDict["lastName"])
        self.assertTrue(userDict["password"])
        self.assertTrue(userDict["created"])

        result2 = self.client.get("/user/"+userDict["id"])
        userDict2 = json.loads(result2.data)
        self.assertTrue(userDict2["id"])

    #TODO: Fix this on a later occation
    @unittest.expectedFailure
    def testPostUserTwice(self):
        result1 = self.client.post("/user", data={"first_name": "John", "last_name": "Skauge", "user_name": "John", "pass": "MyPassword"})
        result2 = self.client.post("/user", data={"first_name": "John", "last_name": "Skauge", "user_name": "John", "pass": "MyPassword"})

        self.fail(msg="Fix this on a later occation")

    def testDeleteUser(self):

        result1 = self.client.post("/user", data={"first_name": "John", "last_name": "Skauge", "user_name": "John", "pass": "MyPassword"})

        userDict = json.loads(result1.data)
        #Id should not leak out, this user dict is used in the ui
        self.assertFalse(hasattr(userDict, "id"), "If this fails the user ID is leaked when created the user. "
                                                  "This should not be returned when creating a user")
        self.assertEquals("John", userDict["firstName"])
        self.assertEquals("Skauge", userDict["lastName"])
        self.assertTrue(userDict["password"])
        self.assertTrue(userDict["created"])

        result2 = self.client.delete("/user/"+ userDict["id"])

        self.assertEquals(202, result2.status_code)


        result3 = self.client.get("/user/"+userDict["id"])

        self.assertEquals(404, result3.status_code)



    @unittest.expectedFailure
    def testRawUserSave(self):
        user = User(firstName="John", lastName="Skauge", userName="John", password="MyPassword")
        # noinspection PyUnresolvedReferences
        self.assertFalse(user.id)
        user.save()
        self.assertTrue(user.id)

        user.delete()

        #this will throw a DoesNotExist error, hence the @unittest.expectedFailure
        user = User.objects.get(id=user.id)





