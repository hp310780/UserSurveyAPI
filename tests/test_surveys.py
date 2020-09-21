import mock

TEST_JSON = "tests/test_data/test_surveys.json"


@mock.patch("os.getenv", return_value=TEST_JSON)
def test_survey_get(mock_db,
                    client):
    """Tests that 1 survey linked to 1 question is returned
    from the survey/ endpoint."""
    id = 1
    response = client.get("/surveys/{}".format(id))
    assert response.status_code == 201
    assert response.json == {
        "id": 1,
        "questions": [
            2
        ]
    }
