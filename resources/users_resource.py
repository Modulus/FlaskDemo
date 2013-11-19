__author__ = 'Modulus'
#coding: utf-8

from flask.ext.restful import Resource, marshal_with

from ..models.user import User


class UsersResource(Resource):

    @marshal_with(User.format())
    def get(self):
        return list(User.objects.all())