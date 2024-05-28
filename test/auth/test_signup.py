from flask.testing import FlaskClient
import pytest

url = "/api/auth/signup"

def test_sign_up_user_already_exits(client: FlaskClient):
    global url
    json = {
        "email": "test@test.com",
        "password": "!@e32z43FyH#"
    }
    response = client.post(url, json=json)
    assert response.status_code == 400
    assert "message" in response.json

@pytest.mark.parametrize("json", [({"email": "ariel#gmail.com", "password": "3259"})])#, ({"email": "ariel@gmail.com", "password": "3259"})])
def test_sign_up_wrong_email_weak_password(json,client: FlaskClient):
    global url
    response = client.post(url, json=json)
    assert response.status_code == 400
    assert "message" in response.json


def test_sign_up(client: FlaskClient):
    global url
    json = {
        "email": "ariel@gmail.com",
        "password": "!@32E85s77"
    }
    response = client.post(url, json=json)
    assert response.status_code == 201
    assert "authType" in response.json
    assert "authToken" in response.json