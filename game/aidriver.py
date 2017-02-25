import pygame


class AIDriver:
    def __init__(self):
        self.results = []
        self.next = 50
        self.last = 50

    def process_input(self, distance, velocity, success, top):
        key_map = {}
        key_map[pygame.K_SPACE] = False
        key_map[pygame.K_RIGHT] = False
        key_map[pygame.K_LEFT] = False
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

            if self.next is 0 and velocity > 0:
                key_map[pygame.K_LEFT] = True
        return key_map
