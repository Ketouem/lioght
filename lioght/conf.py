import os


class DefaultConfiguration(object):

    LIGHT_PROVIDER = os.environ.get('LIOGHT_PROVIDER') or "milight"
    LIGHT_HOST = os.environ.get('LIOGHT_HOST') or "localhost"
    LIGHT_PORT = int(os.environ.get('LIOGHT_PORT')) \
        if os.environ.get('LIOGHT_PORT') else 8899
    LIGHT_OPTS = [] or ["rgbw"]


class DebugConfiguration(DefaultConfiguration):

    DEBUG = True

conf = {
    'default': DefaultConfiguration,
    'debug': DebugConfiguration
}
