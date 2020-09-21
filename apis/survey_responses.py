import json
import os

from flask import request
from flask_restplus import Resource, Namespace, fields

api = Namespace('survey_responses', description='User survey responses')

survey_response_model = api.model('Survey Reponses',
                                  {
                                      'email': fields.String,
                                      'id': fields.Integer
                                  })

create_survey_response_model = api.model('Survey Reponses',
                                         {
                                             'email': fields.String,
                                         })


class SurveyResponseDAO(object):
    """Data Access Object for the Survey Response entity.
    """
    # Mock ID generation as simple counter
    id_generator = 1

    def __init__(self):
        with open(os.getenv("SURVEY_RESPONSES_DB")) as db:
            self.survey_responses = json.load(db)

    @staticmethod
    def _create_id():
        SurveyResponseDAO.id_generator += 1
        return SurveyResponseDAO.id_generator

    def _write(self, survey_response):
        """Write updated response list as in-mem list and to file.

        Args:
            response (list): List of responses currently held.
        """
        self.survey_responses.append(survey_response)

        with open(os.getenv("SURVEY_RESPONSES_DB"), 'w') as outfile:
            json.dump(self.survey_responses, outfile)

    def create(self, data):
        survey_response = data
        survey_response['id'] = self._create_id()
        self.survey_responses.append(survey_response)
        return survey_response


@ api.route('')
class survey_responses(Resource):
    DAO = SurveyResponseDAO()

    @ api.expect(create_survey_response_model)
    def post(self):
        data = request.get_json()
        try:
            survey_response = self.DAO.create(data)
        except TypeError as e:
            api.abort(400, "Unable to create survey response {}".format(e))

        return survey_response, 201
