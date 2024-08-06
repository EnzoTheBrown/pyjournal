import toml


def load_settings():
    with open('pyjournal.toml') as f:
        return toml.load(f)

settings = load_settings()

LOG_DIR = settings['app']['LOG_DIR']
PORT = settings['app']['PORT']
HOST = settings['app']['HOST']
TEMPLATE_FILE = settings['app']['TEMPLATE_FILE']

