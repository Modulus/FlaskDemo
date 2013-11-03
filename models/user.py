from datetime import datetime

__author__ = 'john'


class User(object):
    def __init__(self, **kwargs):
        self.firstName = kwargs["firstName"]
        self.lastName = kwargs["lastName"]
        self.userName = kwargs["userName"]
        self.password = kwargs["password"]
        self.created = None

    def json(self):
        # if self._id:
        #     return {
        #         {
        #             "id": self._id,
        #             "firstName": self.firstName,
        #             "lastName": self.lastName,
        #             "userName": self.userName,
        #             "password": self.password,
        #             "created": self.created
        #         }
        #     }
        return \
            {
                "firstName": self.firstName,
                "lastName": self.lastName,
                "userName": self.userName,
                "password": self.password,
                "created": self.created
            }

