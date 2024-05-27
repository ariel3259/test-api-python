import pytest
from flaskr import create_app

@pytest.fixture
def app():
    config = {
        "SECRET": "loremloremlorem"
    }
    app = create_app(config)
    yield app

@pytest.fixture
def runnet(app):
    return app.test_cli_runner()