from engine.entities.entity import *

""" Vehicle entity. """
class Vehicle(Entity):
    def __init__(self):
        Entity.__init__(self)
        self.velocity = 0

    # Process input to vehicle.
    def process_input(self, input_map):
        if input_map[pygame.K_LEFT]:
            self.brake()
        if input_map[pygame.K_RIGHT]:
            self.accelerate()

    # Increase the velocity.
    def accelerate(self):
        self.velocity += 0.15

    # Reduce the velocity.
    def brake(self):
        if self.velocity > 0:
            self.velocity -= 0.5

        # Clamp the value so we don't go backwards.
        if self.velocity < 0:
            self.velocity = 0

    # Update the vehicle state based on time.
    def update(self):
        self.x += self.velocity
