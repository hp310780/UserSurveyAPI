import mock

TEST_RESPONSE = {
    "email": "mock_user_response@users"
}

TEST_JSON = "tests/test_data/test.json"


@mock.patch("os.getenv", return_value=TEST_JSON)
def test_survey_response_post(mock_db,
                              client):
    """ Tests that a survey response is correctly posted
    to the survey_response endpoint."""

    response = client.post('/survey_responses', json=TEST_RESPONSE)

    TEST_RESPONSE["id"] = 2
    assert response.status_code == 201
    assert response.json == TEST_RESPONSE
