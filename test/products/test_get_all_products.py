import pytest
import requests
from test.products import base_url

def test_get_all_products():
    response = requests.get(base_url)
    rows = response.json()
    row = rows[0]
    assert response.status_code == 200
    assert "name" in row
    assert "price" in row
    assert "stock" in row
