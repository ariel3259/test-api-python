from flask import Blueprint, request
from flaskr.exceptions import HttpException
from flaskr.blueprints.auth import token_required

bp = Blueprint("products", __name__, url_prefix="/api/products")

products = [
    {"id": 1, "name": "manteca", "price": 800, "stock": 10, "is_available": True},
    {"id": 2, "name": "Fideos Marolio", "price": 1200, "stock": 15, "is_available": True},
    {"id": 3, "name": "Biscochos Don Saturn", "price": 898, "stock": 6, "is_available": True},
    {"id": 4, "name": "Biscochos Don Saturn agridulces", "price": 898, "stock": 0, "is_available": False}
]

@bp.get("")
def get_products():
    global products
    tmp_p = products.copy()
    tmp_p = [x.copy() for x in tmp_p if x["is_available"] == True]
    if len(tmp_p) == 0:
        raise HttpException("There aren't products available", 404)
    for i in range(0, len(tmp_p)):
        tmp_p[i].pop("is_available")
    return tmp_p, 200

@bp.post("")
@token_required
def add_products():
    global products
    body = request.json
    if "name" not in body or "price" not in body or "stock" not in body:
        raise HttpException("Name, price and stock fields are mandatory", 400)
    tmp_body = body.copy()
    tmp_body["is_available"] = True
    tmp_body["id"] = len(products) + 1
    products.append(tmp_body)
    return tmp_body, 201

@bp.put("/<int:id>")
@token_required
def update(id):
    global products
    body = request.json        
    
    if 0 <= id > len(products):
        raise HttpException("The product does not exits", 404)
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
    return tmp_product

@bp.delete("/<int:id>")
@token_required
def delete(id):
    global products
    if 0 <= id > len(products):
        raise HttpException("The product does not exits", 404)
    product = products[id - 1]
    if product["is_available"] == False:
        raise HttpException("The product is already deleted", 409)
    product["is_available"] = False
    return "", 204
