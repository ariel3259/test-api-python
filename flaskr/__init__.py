from flask import Flask
from flaskr.blueprints import blueprints
from flaskr.exceptions import HttpException
from dotenv import load_dotenv, find_dotenv
import os

def create_app(test_config):
    load_dotenv(find_dotenv(), override=True)
    app = Flask(__name__)
    app.config["SECRET"] = os.getenv("SECRET")
    if test_config is not None:
        app.config = test_config

    @app.errorhandler(HttpException)
    def handle_http_exception(e: HttpException):
        return {"message": e.message}, e.status_code

    [app.register_blueprint(x) for x in blueprints]
    
    return app
