from flask.testing import FlaskClient

URL = "api/auth/signin"

def test_singin_user_not_exists(client: FlaskClient):
    global URL
    json = {
        "email": "ezequiel@gmail.com",
        "password": "1234"
    }
    response = client.post(URL, json=json)
    assert response.status_code == 404
    assert "message" in response.json

def test_singin_user_wrong_password(client: FlaskClient):
    global URL
    json = {
        "email": "test@test.com",
        "password": "12323"
    }
    response = client.post(URL, json=json)
    assert response.status_code == 400
    assert "message" in response.json

def test_signin(client: FlaskClient):
    global URL
    json = {
        "email": "test@test.com",
        "password": "test"
    }
    response = client.post(URL, json=json)
    assert response.status_code == 200
    assert "authType" in response.json
    assert "authToken" in response.json