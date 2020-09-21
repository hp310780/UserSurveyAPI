import json
import os

from flask_restplus import Resource, Namespace, fields

api = Namespace('surveys', description='User surveys')

survey_model = api.model('Survey', {
    'id': fields.Integer,
    'questions': fields.List(fields.Integer,
                             description='List of question IDs linked to this survey.',
                             required=True)
})


class SurveyDAO(object):
    def __init__(self):
        with open(os.getenv("SURVEYS_DB")) as f:
            self.surveys = json.load(f)

    def get(self, id):
        id = int(id)
        for survey in self.surveys:
            if survey["id"] == id:
                return survey
        return None


@ api.route('/<id>')
class Surveys(Resource):
    DAO = SurveyDAO()

    @ api.marshal_list_with(survey_model)
    def get(self, id):
        survey = self.DAO.get(id)
        if not survey:
            return api.abort(404, "Survey {} not found.".format(id))
        return survey, 201
