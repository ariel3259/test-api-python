from flask.testing import FlaskClient

authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzM1MzkwNjgzfQ.tVarhlzfs7EksiTIUNfZGB8DpiOHG7Pd95VfftRq9sRChv1B2w3zrtHOdPse-Alp0BX_O9xxv_Ad_35YqPM_Pg"
url = "/api/products/{}"

def test_delete_product_unauthorized(client: FlaskClient):
    global url
    id = 3
    response = client.delete(url.format(id))
    assert response.status_code == 401
    assert "message" in response.json

def test_delete_product_not_exits(client: FlaskClient):
    global url
    global authorization
    id = 8
    response = client.delete(url.format(id), headers={"Authorization": authorization})
    assert response.status_code == 404
    assert "message" in response.json

def test_delete_product_deleted(client: FlaskClient):
    global url
    global authorization
    id=4
    response = client.delete(url.format(id), headers={"Authorization": authorization})
    assert response.status_code == 409
    assert "message" in response.json

def test_deleted_product(client: FlaskClient): 
    global url
    global authorization
    id = 3
    response = client.delete(url.format(id), headers={"Authorization": authorization})
    assert response.status_code == 204
