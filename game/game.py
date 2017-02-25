from engine.gamebase import GameBase


class Game(GameBase):
    def __init__(self, config, clock):
        GameBase.__init__(self, config, clock)

        self.car = None

    def initialise(self, data):
        GameBase.initialise(self, data)

        self.car = self.entityManager.find_entity("car")
        self.inputHandler.set_focus(self.car)

    def handle_input(self):
        GameBase.handle_input(self)

    def update(self):
        GameBase.update(self)

        # Stop the car from falling off the edge.
        if self.car.x > self.config.width - self.car.width:
            self.car.velocity = 0
            self.car.x = self.config.width - self.car.width

    def render(self, screen):
        GameBase.render(self, screen)
