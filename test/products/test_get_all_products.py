from flask.testing import FlaskClient

def test_get_all_products(client: FlaskClient):
    response = client.get("/api/products")
    
    assert response.status_code == 200
    assert len(response.json) > 0
    assert "name" in response.json[0]
    assert "price" in response.json[0]
    assert "stock" in response.json[0]
