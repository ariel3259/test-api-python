from flaskr.blueprints import products, auth
from flask import Blueprint

blueprints: list[Blueprint] = [
    products.bp,
    auth.bp
]