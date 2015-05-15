from milight import MiLight, LightBulb

from . import LightController


class MiLightController(LightController):

    def __init__(self, host, port, bulbs, *args, **kwargs):
        super(MiLightController, self).__init__(*args, **kwargs)
        self._milight = MiLight({'host': host, 'port': port}, wait_duration=0)
        self._bulbs = LightBulb(bulbs)

    def switch_on(self, light_id):
        self._milight.send(self._bulbs.on(light_id))

    def switch_off(self, light_id):
        self._milight.send(self._bulbs.off(light_id))
