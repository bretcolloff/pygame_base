import pygame


class Entity:
    def __init__(self):
        self.image = None
        self.x = None
        self.y = None
        self.visible = False

    def load(self, data):
        resources = data['resources']

        self.image = pygame.image.load(resources['image']).convert()

        if 'position' in data:
            position = data['position']
            self.x = position['x']
            self.y = position['y']
            self.visible = True
        else:
            self.x = None
            self.y = None
            self.visible = False

    def render(self, screen):
        if self.visible:
            screen.blit(self.image, (self.x, self.y))
