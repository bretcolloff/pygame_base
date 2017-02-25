from engine.entities.entity import *
from engine.resource_managers.entitymanager import *

from inputhandler import *


class Game():
    def __init__(self, config, clock):
        # TODO push into the engine
        self.entityManager = None
        self.inputHandler = None
        self.config = config
        self.clock = clock
        # TODO end

        self.car = None

    def initialise(self):
        # TODO push into the engine
        self.entityManager = EntityManager()
        self.entityManager.load('resources/data/data.json')

        # TODO game logic
        self.car = self.entityManager.find_entity("car")
        # TODO end

        self.inputHandler = InputHandler()
        self.inputHandler.set_focus(self.car)
        # TODO end

    def handle_input(self):
        # TODO push into the engine
        self.inputHandler.apply_input(pygame.key.get_pressed())
        # TODO end

    def update(self):
        # TODO push into the engine
        for entity in self.entityManager.entities:
            entity.update()
        # TODO end

        # Stop the car from falling off the edge.
        if self.car.x > self.config.width - self.car.width:
            self.car.velocity = 0
            self.car.x = self.config.width - self.car.width

        # TODO push into the engine
        # Update the clock
        self.clock.tick(30)
        # TODO end

    def render(self, screen):
        # TODO push into the engine
        for entity in self.entityManager.entities:
            entity.render(screen)
        # TODO end