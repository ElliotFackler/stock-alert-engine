import json

def load_config_json():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

APP_CONFIG = load_config_json()
