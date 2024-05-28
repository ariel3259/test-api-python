import pytest
from flaskr import create_app
from flask import Flask

@pytest.fixture()
def app():
    config = {
        "TESTING": True,
        "SECRET": "loremloremlorem",
        "APPLICATION_ROOT": "/"
    }
    app = create_app(config)

    yield app

@pytest.fixture()
def runner(app: Flask):
    return app.test_cli_runner()

@pytest.fixture()
def client(app: Flask):
    return app.test_client()