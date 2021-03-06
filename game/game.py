import pygame

from engine.gamebase import GameBase
from game.aidriver import AIDriver


""" The core logic for the driving simulation. """
class Game(GameBase):
    def __init__(self, config, clock):
        GameBase.__init__(self, config, clock)

        self.car = None
        self.topSpeed = 0
        self.topValid = 0
        self.distance = 0
        self.success = True
        self.aiRun = True
        self.aiDriver = None

    # Initialise driving game elements.
    def initialise(self, data):
        GameBase.initialise(self, data)

        self.success = True
        self.topSpeed = 0

        self.car = self.entityManager.find_entity("car")
        self.inputHandler.set_focus(self.car)
        self.distance = (self.config.width - 50) - (self.car.x + 25)

        self.aiDriver = AIDriver()
        self.aiDriver.train_ai(self.distance, self.car)

    # Handle the human or AI input.
    def handle_input(self):
        if not self.aiRun:
            GameBase.handle_input(self)
        else:
            # Have the AI populate the input map.
            self.input_map = self.aiDriver.process_input(self.car.velocity)
            self.inputHandler.apply_input(self.input_map)

        if self.input_map[pygame.K_SPACE] and self.car.velocity is 0:
            self.reset()

    # Update driving game specific logic.
    def update(self):
        GameBase.update(self)

        if self.car.velocity > self.topSpeed:
            self.topSpeed = self.car.velocity

        # Stop the car from falling off the edge.
        if self.car.x > self.config.width - 75: # The width of the wall
            self.car.velocity = 0
            self.topSpeed = 0
            self.success = False

        # Update distance
        self.distance = (self.config.width - 50) - (self.car.x + 25)

    # Render additional driving game specific entities.
    def render(self, screen, font):
        GameBase.render(self, screen, font)

        # Render text
        textsurface = font.render('Speed: ' + str(self.car.velocity)[:5], False, (0, 30, 0))
        screen.blit(textsurface, (0, 0))
        textsurface = font.render('Top: ' + str(self.topValid)[:5], False, (0, 30, 0))
        screen.blit(textsurface, (0, 30))
        textsurface = font.render('Distance: ' + str(self.distance)[:5], False, (0, 30, 0))
        screen.blit(textsurface, (0, 60))
        if not self.success:
            textsurface = font.render('Failed', False, (255, 0, 0))
            screen.blit(textsurface, (350, 0))

    # Reset elements of the driving simulation for 'retrying'.
    def reset(self):
        if self.success:
            if self.topSpeed > self.topValid:
                self.topValid = self.topSpeed
        self.initialise(self.datafile)