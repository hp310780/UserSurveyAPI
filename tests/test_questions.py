import mock

TEST_JSON = "tests/test_data/test_questions.json"


@mock.patch("os.getenv", return_value=TEST_JSON)
def test_question_get(mock_db,
                      client):
    """ Tests that getting a question returns
    the correct question. """
    id = 2
    response = client.get("/questions/{}".format(id))
    assert response.status_code == 201
    assert response.json == {
        "id": 2,
        "question": "What is your location?",
        "response_type": "multiple_choice",
        "response_accepted": [
            "UK",
            "Australia",
            "Singapore"
        ]
    }
