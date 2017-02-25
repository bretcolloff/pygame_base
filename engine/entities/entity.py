import pygame


class Entity:
    def __init__(self):
        self.image = None
        self.x = None
        self.y = None
        self.width = None
        self.height = None
        self.visible = False
        self.id = ""
        self.static = False
        self.visible = False

    def load(self, data):
        resources = data['resources']

        self.image = pygame.image.load(resources['image']).convert()

        if 'position' in data:
            position = data['position']
            self.x = position['x']
            self.y = position['y']
        else:
            self.x = None
            self.y = None

        if 'properties' in data:
            properties = data['properties']
            self.id = properties['id']
            self.static = properties['static']
            self.visible = properties['visible']

        if 'size' in data:
            size = data['size']
            self.width = size['width']
            self.height = size['height']

    def render(self, screen):
        if self.visible:
            screen.blit(self.image, (self.x, self.y))

    def process_input(self, input_map):
        if input_map[pygame.K_UP]:
            self.y -= 1
        if input_map[pygame.K_DOWN]:
            self.y += 1
        if input_map[pygame.K_LEFT]:
            self.x -= 1
        if input_map[pygame.K_RIGHT]:
            self.x += 1

    def update(self):
        return
