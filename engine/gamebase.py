from engine.entities.entity import *
from engine.inputhandler import *
from engine.resource_managers.entitymanager import *

""" Base class for running the game, handles loading, updating, input, rendering etc. """
class GameBase:
    def __init__(self, config, clock):
        self.entityManager = None
        self.inputHandler = None
        self.config = config
        self.clock = clock
        self.datafile = ""
        self.input_map = []

    # Carry out game state initialisation.
    def initialise(self, data):
        self.datafile = data
        self.entityManager = EntityManager()
        self.entityManager.load(data)

        self.inputHandler = InputHandler()

    # Process keyboard input.
    def handle_input(self):
        self.input_map = pygame.key.get_pressed()
        self.inputHandler.apply_input(self.input_map)

    # Update entities.
    def update(self):
        self.clock.tick(30)

        for entity in self.entityManager.entities:
            entity.update()

    # Render entities.
    def render(self, screen, font):
        for entity in self.entityManager.entities:
            entity.render(screen)

    # Reset the state.
    def reset(self):
        self.initialise(self.datafile)