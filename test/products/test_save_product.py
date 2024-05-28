from flask.testing import FlaskClient

authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzM1MzkwNjgzfQ.tVarhlzfs7EksiTIUNfZGB8DpiOHG7Pd95VfftRq9sRChv1B2w3zrtHOdPse-Alp0BX_O9xxv_Ad_35YqPM_Pg"
url = "/api/products"

def test_save_product_unauthorized(client: FlaskClient):
    global url
    product = {
        "name": "Shampoo Sedal",
        "price": 1500,
        "stock": 6
    }
    response = client.post(url, json=product)
    assert response.status_code == 401
    assert "message" in response.json

def test_save_product_field_empty(client: FlaskClient):
    global authorization
    global url
    product = {
        "price": 1500,
        "stock": 6
    }
    response = client.post(url, json=product, headers = {"Authorization": authorization})
    assert response.status_code == 400
    assert "message" in response.json

def test_save_product(client: FlaskClient):
    global url
    global authorization
    product = {
        "name": "Shampoo Sedal",
        "price": 1500,
        "stock": 6
    }
    response = client.post(url, json=product, headers = {"Authorization": authorization})
    assert response.status_code == 201
    assert "id" in response.json
    assert "name" in response.json
    assert "price" in response.json
    assert "stock" in response.json