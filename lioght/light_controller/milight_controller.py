from milight import MiLight, LightBulb, color_from_hex

from . import LightController


class MiLightController(LightController):

    VENDOR = "milight"

    def __init__(self, host, port, bulbs, *args, **kwargs):
        super(MiLightController, self).__init__(*args, **kwargs)
        self._milight = MiLight({'host': host, 'port': int(port)},
                                wait_duration=0)
        self._bulbs = LightBulb(bulbs)

    def switch_on(self, light_id):
        self._milight.send(self._bulbs.on(light_id))

    def switch_all_on(self):
        self._milight.send(self._bulbs.all_on())

    def switch_off(self, light_id):
        self._milight.send(self._bulbs.off(light_id))

    def switch_all_off(self):
        self._milight.send(self._bulbs.all_off())

    def change_color(self, light_id, color_code):
        self._milight.send(
            self._bulbs.color(color_from_hex(color_code), light_id))
