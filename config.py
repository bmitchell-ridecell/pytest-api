import configparser
import os

config = configparser.ConfigParser()
config.read('config.ini')

# TODO add command line arg for target environment
env_name = "DARWIN-QA"

# Get key for environment with fallback to default if not found
def get(key):
    if config[env_name][key] is not None:
        return config[env_name][key]
    return config['DEFAULT'][key]

