import mock

TEST_USER = {
    "email": "mock_user@users"
}

TEST_JSON = "tests/test_data/test.json"


@mock.patch("os.getenv", return_value=TEST_JSON)
def test_user_get(mock_db,
                  client):
    """ Tests that getting users returns the
    correct empty db of users."""
    response = client.get("/users")
    assert response.status_code == 200
    assert response.json == []


@mock.patch("os.getenv", return_value=TEST_JSON)
def test_user_post(mock_db,
                   client):
    """ Tests that posting a user returns the correct
    user."""
    response = client.post('/users', json=TEST_USER)

    TEST_USER["id"] = 2
    assert response.status_code == 201
    assert response.json == TEST_USER
