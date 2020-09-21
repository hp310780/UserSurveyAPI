from flask_restplus import Api

from .users import api as users_api
from .questions import api as question_api
from .surveys import api as survey_api
from .survey_responses import api as survey_response_api

api = Api(
    title='User Information API',
    version='1.0.0',
    description='An API for gathering user information.',
)

api.add_namespace(users_api)
api.add_namespace(question_api)
api.add_namespace(survey_api)
api.add_namespace(survey_response_api)
