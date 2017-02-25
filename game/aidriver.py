import pygame

""" Takes input and provides decisions for driving the simulation. """
class AIDriver:
    def __init__(self):
        self.results = []

        # The number of remaining simulation steps.
        self.next = 78

        # The total number of acceleration steps from the last attempt.
        self.last = 78

    #Provides input responses based on the simulation state.
    def process_input(self, distance, velocity, success, top):
        key_map = {}
        key_map[pygame.K_SPACE] = False
        key_map[pygame.K_RIGHT] = False
        key_map[pygame.K_LEFT] = False

        # If we applied too much power, try less next time.
        if success is False:
            key_map[pygame.K_SPACE] = True
            self.next = self.last - 2
            self.last = self.last - 2
            return key_map
        else:
            if self.next is 0 and velocity is 0:
                self.results.append((self.last, top))
                self.next = self.last + 1
                self.last = self.last + 1
                key_map[pygame.K_SPACE] = True
                return key_map
            if self.next > 0:
                self.next -= 1
                key_map[pygame.K_RIGHT] = True
                return key_map

            # Put the brakes on.
            if self.next is 0 and velocity > 0:
                key_map[pygame.K_LEFT] = True
        return key_map
