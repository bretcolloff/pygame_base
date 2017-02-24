import json

from engine.entities.entity import Entity


class EntityManager:
    def __init__(self):
        self.entities = []

    def load(self, path):
        data = []
        with open(path) as data_file:
            data = json.load(data_file)

        if 'entities' in data:
            for entityData in data['entities']:
                entity = Entity()
                entity.load(entityData)

                self.entities.append(entity)
