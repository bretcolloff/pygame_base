from engine.entities.entity import *
from engine.resource_managers.entitymanager import *

from inputhandler import *


class GameBase:
    def __init__(self, config, clock):
        self.entityManager = None
        self.inputHandler = None
        self.config = config
        self.clock = clock
        self.datafile = ""
        self.input_map = []

    def initialise(self, data):
        self.datafile = data
        self.entityManager = EntityManager()
        self.entityManager.load(data)

        self.inputHandler = InputHandler()

    def handle_input(self):
        self.input_map = pygame.key.get_pressed()
        self.inputHandler.apply_input(self.input_map)

    def update(self):
        self.clock.tick(30)

        for entity in self.entityManager.entities:
            entity.update()

    def render(self, screen, font):
        for entity in self.entityManager.entities:
            entity.render(screen)

    def reset(self):
        self.initialise(self.datafile)