import pytest
import json

TEST_JSON = "tests/test_data/test.json"
QUESTION_JSON = "tests/test_data/test_questions.json"
SURVEY_JSON = "tests/test_data/test_surveys.json"


@pytest.fixture(autouse=True, scope="function")
def setUp():
    yield

    # Reset test json to empty after each test
    with open(TEST_JSON, 'w') as outfile:
        json.dump([], outfile)


@pytest.fixture
def app():
    from app import create_app

    app = create_app("tests/.testenv")
    return app
