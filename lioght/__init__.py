from flask import Flask, g

from light_controller import LightControllerRegistry
from conf import conf


def create_app(deploy_type="default"):

    app = Flask(__name__)
    config_o = conf[deploy_type]
    app.config.from_object(config_o)

    @app.before_request
    def before_request():
        controller_cls = LightControllerRegistry.get_controller_class(
            config_o.LIGHT_PROVIDER)
        g.controller = controller_cls(*[config_o.LIGHT_HOST,
                                        config_o.LIGHT_PORT,
                                        config_o.LIGHT_OPTS])

    from api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
