from flask.testing import FlaskClient

def test_save_product_unauthorized(client: FlaskClient):
    product = {
        "name": "Shampoo Sedal",
        "price": 1500,
        "stock": 6
    }
    response = client.post("/api/products", json=product)
    assert response.status_code == 401
    assert "message" in response.json

def test_save_product_field_empty(client: FlaskClient):
    authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzE2ODc3OTU1fQ.YfmRoVGmKvA4wkFjwZu1sUu8H7mNU677IibHOI68--xGtV4vujToM0zZjUEQ6WHh-dg0_Vd094X-XKBWTgstxw"
    product = {
        "price": 1500,
        "stock": 6
    }
    response = client.post("/api/products", json=product, headers = {"Authorization": authorization})
    assert response.status_code == 400
    assert "message" in response.json

def test_save_product(client: FlaskClient):
    authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzE2ODc3OTU1fQ.YfmRoVGmKvA4wkFjwZu1sUu8H7mNU677IibHOI68--xGtV4vujToM0zZjUEQ6WHh-dg0_Vd094X-XKBWTgstxw"
    product = {
        "name": "Shampoo Sedal",
        "price": 1500,
        "stock": 6
    }
    response = client.post("/api/products", json=product, headers = {"Authorization": authorization})
    assert response.status_code == 201
    assert "id" in response.json
    assert "name" in response.json
    assert "price" in response.json
    assert "stock" in response.json