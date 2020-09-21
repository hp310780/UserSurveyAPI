import json
import os

from flask import request
from flask_restplus import Resource, Namespace, fields

api = Namespace('users', description='User operations')

user_model = api.model('User',
                       {
                           'email': fields.String,
                           'id': fields.Integer
                       })

create_user_model = api.model('User',
                              {
                                  'email': fields.String,
                              })


class UserDAO(object):
    """Data Access Object for the User entity.

    Note we are mocking a user DB through a .json file
    specified in the .env.
    """

    # Mock ID generation as simple counter
    id_generator = 1

    def __init__(self):
        with open(os.getenv("USERS_DB")) as db:
            self.users = json.load(db)

    @staticmethod
    def _create_id():
        UserDAO.id_generator += 1
        return UserDAO.id_generator

    def _write(self, user):
        """Write updated users list as in-mem list and to file.

        Args:
            user (list): List of users currently held.
        """
        self.users.append(user)
        with open(os.getenv("USERS_DB"), 'w') as outfile:
            json.dump(self.users, outfile)

    def get(self):
        return self.users

    def create(self, data):
        user = data
        user['id'] = self._create_id()
        self._write(user)
        return user


@ api.route('')
class Users(Resource):
    DAO = UserDAO()

    @ api.marshal_list_with(user_model)
    def get(self):
        return self.DAO.users, 200

    @ api.expect(create_user_model)
    def post(self):
        data = request.get_json()

        try:
            user = self.DAO.create(data)
        except TypeError as e:
            api.abort(400, "Unable to create user {}".format(e))

        return user, 201
