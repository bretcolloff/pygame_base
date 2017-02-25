from engine.entities.entity import *


class Vehicle(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.velocity = 0

    def process_input(self, input_map):
        if input_map[pygame.K_LEFT]:
            self.brake()
        if input_map[pygame.K_RIGHT]:
            self.accelerate()

    def accelerate(self):
        self.velocity += 0.01

    def brake(self):
        if self.velocity > 0:
            self.velocity -= 0.05

        # Clamp the value so we don't go backwards.
        if self.velocity < 0:
            self.velocity = 0

    def update(self):
        self.x += self.velocity
