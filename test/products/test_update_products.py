from flask.testing import FlaskClient

authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzM1MzkwNjgzfQ.tVarhlzfs7EksiTIUNfZGB8DpiOHG7Pd95VfftRq9sRChv1B2w3zrtHOdPse-Alp0BX_O9xxv_Ad_35YqPM_Pg"
url = "/api/products/{}"

def test_update_product_unauthorized(client: FlaskClient):
    global url
    product = {
        "price": 1400
    }
    id = 2
    response = client.put(url.format(id), json=product)
    assert response.status_code == 401
    assert "message" in response.json

def test_update_product_field_required(client: FlaskClient):
    global url
    global authorization
    id = 2
    response = client.put(url.format(id), json={}, headers={"Authorization": authorization})
    assert response.status_code == 400
    assert "message" in response.json

def test_update_product_not_exits(client: FlaskClient):
    global url
    global authorization
    id = 8
    response = client.put(url.format(id), json={}, headers={"Authorization": authorization})
    assert response.status_code == 404
    assert "message" in response.json

def test_update_product(client: FlaskClient):
    global url
    global authorization
    product = {
        "price": 1400
    }
    id = 2
    response = client.put(url.format(id), json=product, headers={"Authorization": authorization})
    assert response.status_code == 200
    assert "id" in response.json
    assert "name" in response.json
    assert "price" in response.json
    assert "stock" in response.json
    assert "is_available" not in response.json
