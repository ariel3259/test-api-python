from flask.testing import FlaskClient

def test_update_product_unauthorized(client: FlaskClient):
    product = {
        "price": 1400
    }
    id = 2
    response = client.put(f"/api/products/{id}", json=product)
    assert response.status_code == 401
    assert "message" in response.json

def test_update_product_field_required(client: FlaskClient):
    authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzE2ODc3OTU1fQ.YfmRoVGmKvA4wkFjwZu1sUu8H7mNU677IibHOI68--xGtV4vujToM0zZjUEQ6WHh-dg0_Vd094X-XKBWTgstxw"
    id = 2
    response = client.put(f"/api/products/{id}", json={}, headers={"Authorization": authorization})
    assert response.status_code == 400
    assert "message" in response.json

def test_update_product_not_exits(client: FlaskClient):
    authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzE2ODc3OTU1fQ.YfmRoVGmKvA4wkFjwZu1sUu8H7mNU677IibHOI68--xGtV4vujToM0zZjUEQ6WHh-dg0_Vd094X-XKBWTgstxw"
    id = 8
    response = client.put(f"/api/products/{id}", json={}, headers={"Authorization": authorization})
    assert response.status_code == 404
    assert "message" in response.json

def test_update_product(client: FlaskClient):
    product = {
        "price": 1400
    }
    id = 2
    authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzE2ODc3OTU1fQ.YfmRoVGmKvA4wkFjwZu1sUu8H7mNU677IibHOI68--xGtV4vujToM0zZjUEQ6WHh-dg0_Vd094X-XKBWTgstxw"
    response = client.put(f"/api/products/{id}", json=product, headers={"Authorization": authorization})
    assert response.status_code == 200
    assert "id" in response.json
    assert "name" in response.json
    assert "price" in response.json
    assert "stock" in response.json
    assert "is_available" not in response.json
