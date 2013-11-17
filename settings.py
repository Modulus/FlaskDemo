import urlparse
import os

__author__ = 'modulus'

MONGOHQ_URL = os.environ.get('MONGOHQ_URL')


if MONGOHQ_URL:
    url = urlparse.urlparse(MONGOHQ_URL)
    MONGODB_USERNAME = url.username
    MONGODB_PASSWORD = url.password
    MONGODB_HOST =  url.hostname
    MONGODB_PORT = url.port
    MONGODB_DB = url.path[1:]
else:
    MONGODB_HOST = "localhost"
    MONGODB_PORT = "27017"
    MONGODB_DB = "demo"
