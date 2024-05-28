from flask.testing import FlaskClient

def test_delete_product_unauthorized(client: FlaskClient):
    id = 3
    response = client.delete(f"/api/products/{id}")
    assert response.status_code == 401
    assert "message" in response.json

def test_delete_product_not_exits(client: FlaskClient):
    id = 8
    authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzE2ODc3OTU1fQ.YfmRoVGmKvA4wkFjwZu1sUu8H7mNU677IibHOI68--xGtV4vujToM0zZjUEQ6WHh-dg0_Vd094X-XKBWTgstxw"
    response = client.delete(f"/api/products/{id}", headers={"Authorization": authorization})
    assert response.status_code == 404
    assert "message" in response.json

def test_delete_product_deleted(client: FlaskClient):
    id=4
    authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzE2ODc3OTU1fQ.YfmRoVGmKvA4wkFjwZu1sUu8H7mNU677IibHOI68--xGtV4vujToM0zZjUEQ6WHh-dg0_Vd094X-XKBWTgstxw"
    response = client.delete(f"/api/products/{id}", headers={"Authorization": authorization})
    assert response.status_code == 409
    assert "message" in response.json

def test_deleted_product(client: FlaskClient):  
    authorization = "Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyIiwiZW1haWwiOiJ0ZXN0QHRlc3QuY29tIiwiaWF0IjoxNzE2ODc3OTU1fQ.YfmRoVGmKvA4wkFjwZu1sUu8H7mNU677IibHOI68--xGtV4vujToM0zZjUEQ6WHh-dg0_Vd094X-XKBWTgstxw"
    id = 3
    response = client.delete(f"/api/products/{id}", headers={"Authorization": authorization})
    assert response.status_code == 204
