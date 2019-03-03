import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

# TODO add command line arg for target environment
env_name = "EIFFEL-QA"
base_url = config[env_name]["base_url"]

# Get key from DEFAULT if not found in current environment
def get(key):
    if config[env_name][key] is not None:
        return config[env_name][key]
    return config['DEFAULT'][key]

