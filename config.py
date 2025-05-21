
import json

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def update_config(key, value):
    config = load_config()
    config[key] = value
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
