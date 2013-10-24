__author__ = 'john'


class User(object):
    def __init__(self, **kwargs):
        self.firstName = kwargs["firstName"]
        self.lastName = kwargs["lastName"]
        self.userName = kwargs["userName"]
        self.password = kwargs["password"]
        self.created = kwargs["created"]

    def json(self):
        return \
            {
                "firstName": self.firstName,
                "lastName": self.lastName,
                "userName": self.userName,
                "password": self.password,
                "created": self.created
            }

