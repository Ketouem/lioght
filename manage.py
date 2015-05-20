from flask.ext.script import Manager, Shell, Server

from lioght import create_app
from lioght.light_controller import LightControllerRegistry
from lioght.light_controller.milight_controller import MiLightController


app = create_app('debug')
manager = Manager(app)


def _make_shell_context():
    return dict(LightControllerRegistry=LightControllerRegistry,
                MiLightController=MiLightController,
                app=app)

manager.add_command("shell", Shell(make_context=_make_shell_context))
manager.add_command("debug", Server())

if __name__ == "__main__":
    manager.run()
