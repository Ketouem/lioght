from flask import Flask, g

from light_controller import LightControllerRegistry


def create_app():

    app = Flask(__name__)

    @app.before_request
    def before_request():
        g.registry = LightControllerRegistry

    return app
