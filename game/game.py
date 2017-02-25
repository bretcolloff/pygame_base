from engine.gamebase import GameBase
import pygame

class Game(GameBase):
    def __init__(self, config, clock):
        GameBase.__init__(self, config, clock)

        self.car = None
        self.topSpeed = 0
        self.topValid = 0
        self.success = True

    def initialise(self, data):
        GameBase.initialise(self, data)

        self.success = True
        self.car = self.entityManager.find_entity("car")
        self.inputHandler.set_focus(self.car)

    def handle_input(self):
        GameBase.handle_input(self)

        if self.input_map[pygame.K_SPACE] and self.car.velocity is 0:
            self.reset()

    def update(self):
        GameBase.update(self)

        if self.car.velocity > self.topSpeed:
            self.topSpeed = self.car.velocity

        # Stop the car from falling off the edge.
        if self.car.x > self.config.width - 75: # The width of the wall
            self.car.velocity = 0
            self.topSpeed = 0
            self.success = False

    def render(self, screen, font):
        GameBase.render(self, screen, font)

        # Render text
        textsurface = font.render('Speed: ' + str(self.car.velocity)[:5], False, (0, 30, 0))
        screen.blit(textsurface, (0, 0))
        textsurface = font.render('Top: ' + str(self.topValid)[:5], False, (0, 30, 0))
        screen.blit(textsurface, (0, 30))
        if not self.success:
            textsurface = font.render('Failed', False, (255, 0, 0))
            screen.blit(textsurface, (350, 0))

    def reset(self):
        if self.success:
            if self.topSpeed > self.topValid:
                self.topValid = self.topSpeed
        self.initialise(self.datafile)