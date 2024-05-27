from flask import Blueprint, request
from flaskr.exceptions import HttpException
from flaskr.blueprints.auth import token_required
bp = Blueprint("products", __name__, url_prefix="/api/products")

products = [
    {"id": 1, "name": "manteca", "price": 800, "stock": 10, "is_available": True},
    {"id": 2, "name": "Fideos Marolio", "price": 1200, "stock": 15, "is_available": True},
    {"id": 3, "name": "Biscochos Don Saturn", "price": 898, "stock": 6, "is_available": True}
]

@bp.get()
def get_products():
    global products
    tmp_p = products.copy()
    tmp_p = [x for x in tmp_p if x["is_available"] == True]
    if len(tmp_p) == 0:
        raise HttpException("There aren't products available", 404)
    for i in range(0, len(tmp_p)):
        tmp_p[i].pop("is_available")
    return tmp_p, 200

@bp.post()
@token_required
def add_products():
    global products
    body = request.json
    if "name" not in body or "price" not in body or "stock" not in body:
        raise HttpException("Name, price and stock fields are mandatory", 400)
    body.is_available = True
    body.id = len(products) + 1
    products.append(body)
    return body, 201

@bp.put("/<int:id>")
@token_required
def update(id):
    global products
    body = request.json
    if len(body.keys()) == 0:
        raise HttpException("needs field for the update", 400)
    product = products[id - 1]
    if product["is_available"] is False:
        raise HttpException("The product is no longer available", 404)
    
    product["name"] = body["name"] if "name" in body else product["name"]
    product["price"] = body["price"] if "price" in body else product["price"]
    product["stock"] = body["stock"] if "stock" in body else product["stock"]
    product["is_available"] = False if product["stock"] == 0 else product["is_available"]
    tmp_product = product.copy()
    tmp_product.pop("is_available")
    return product

@bp.delete("/<int:id>")
@token_required
def delete(id):
    global products
    product = products[id - 1]
    if product is None:
        raise HttpException("The product does not exits", 404)
    elif product["is_available"] is False:
        raise HttpException("The product is already deleted", 409)
    product.is_available = False
    return None, 204
