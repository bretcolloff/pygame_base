from engine.entities.entity import *
from engine.resource_managers.entitymanager import *

from inputhandler import *


class Game():
    def __init__(self):
        self.entityManager = None
        self.inputHandler = None

    def initialise(self):
        self.entityManager = EntityManager()
        self.entityManager.load('resources/data/data.json')

        self.inputHandler = InputHandler()
        self.inputHandler.set_focus(self.entityManager.entities[0])

    def handle_input(self):
        self.inputHandler.apply_input(pygame.key.get_pressed())

    def update(self):
        for entity in self.entityManager.entities:
            entity.update()

    def render(self, screen):
        for entity in self.entityManager.entities:
            entity.render(screen)
