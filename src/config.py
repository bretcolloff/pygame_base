import json


class Config:
    def __init__(self, path):
        config = []
        with open(path) as config_file:
            config = json.load(config_file)

        self.width = config['application']['resolution']['width']
        self.height = config['application']['resolution']['height']
        self.name = config['application']['name']
