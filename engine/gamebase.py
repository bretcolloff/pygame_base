from engine.entities.entity import *
from engine.resource_managers.entitymanager import *

from inputhandler import *


class GameBase:
    def __init__(self, config, clock):
        self.entityManager = None
        self.inputHandler = None
        self.config = config
        self.clock = clock

    def initialise(self, data):
        self.entityManager = EntityManager()
        self.entityManager.load(data)

        self.inputHandler = InputHandler()

    def handle_input(self):
        self.inputHandler.apply_input(pygame.key.get_pressed())

    def update(self):
        self.clock.tick(30)

        for entity in self.entityManager.entities:
            entity.update()

    def render(self, screen):
        for entity in self.entityManager.entities:
            entity.render(screen)