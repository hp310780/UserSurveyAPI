import json
import enum
import os

from flask_restplus import Resource, Namespace, fields

api = Namespace('questions', description='User questions')


class EnumQuestionType(enum.Enum):
    """Accepted question response types"""
    string = 'string'
    multiple_choice = 'list'
    number = 'number'


question_model = api.model('Question',
                           {
                               'id': fields.Integer,
                               'question': fields.String,
                               'response_type': fields.String(
                                   description='Accepted response type',
                                   enum=EnumQuestionType.__members__.items()),
                               'response_accepted': fields.List
                           })


class QuestionDAO(object):
    """Questions Data Access Object.

    We are mocking the question db through a .json
    specified in the .env.
    """

    def __init__(self):

        with open(os.getenv("QUESTIONS_DB")) as f:
            self.questions = json.load(f)

    def get(self, id):
        id = int(id)
        for question in self.questions:
            if question["id"] == id:
                return question
        return None


@ api.route('/<id>')
class Questions(Resource):
    DAO = QuestionDAO()

    def get(self, id):
        question = self.DAO.get(id)
        if not question:
            return api.abort(404, "Question {} not found".format(id))

        return question, 201
