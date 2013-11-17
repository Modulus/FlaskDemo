from unittest import TestCase
from flask_app import app, createApp

__author__ = 'modulus'




class UserResouceTest(TestCase):

    app = createApp("test_settings")




    def testDB(self):
        self.assertEquals("demo_test", app.config["MONGODB_DB"])

    def test_post_user(self):

        with app.test_client() as client:
            result = client.post("/user", data={"first_name": "John", "last_name": "Skauge", "user_name": "John", "pass": "MyPassword"})


        x = 0

        # client.post()
        # user = User()
        # user.firstName = "John"
        # user.lastName = "Skauge"
        # user.userName = "John"
        # user.password = "passwd"
        #
        # user.save()

