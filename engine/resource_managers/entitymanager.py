import importlib
import json

from engine.entities.entity import Entity

""" Manages game entities. """
class EntityManager:
    def __init__(self):
        self.entities = []

    # Load game entities from config.
    def load(self, path):
        data = []
        with open(path) as data_file:
            data = json.load(data_file)

        if 'entities' in data:
            for entityData in data['entities']:
                if 'specialisation' in entityData['properties']:
                    entity = self.instantiate_specialisation(entityData)
                    self.entities.append(entity)
                else:
                    entity = Entity()
                    entity.load(entityData)

                    self.entities.append(entity)

    # Instantiate a specialised entity by module name.
    def instantiate_specialisation(self, entityData):
        module = entityData['properties']['specialisation_module']
        specialisation = entityData['properties']['specialisation']

        Specialisation = getattr(importlib.import_module(module), specialisation)
        instance = Specialisation()
        instance.load(entityData)
        return instance

    # Find an entity by it's id.
    def find_entity(self, id):
        for entity in self.entities:
            if entity.id == id:
                return entity
        return None
