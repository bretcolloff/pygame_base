import pygame

from engine.config import *
from engine.entities.entity import *
from engine.resource_managers.entitymanager import *

from inputhandler import *

# initialize game engine
pygame.init()

# Load config
config = Config('resources/data/config.json')
# set screen width/height and caption

screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.name)

# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# Load entites
entityManager = EntityManager()
entityManager.load('resources/data/data.json')

inputHandler = InputHandler()
inputHandler.set_focus(entityManager.entities[0])

# Game loop
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Process input
    inputHandler.apply_input(pygame.key.get_pressed())

    # write game logic here
    for entity in entityManager.entities:
        entity.update()

    # Clear the screen.
    screen.fill((100, 149, 237))

    # write draw code here
    for entity in entityManager.entities:
        entity.render(screen)

    pygame.display.update()
    # run at 30 fps
    clock.tick(30)

# close the window and quit
pygame.quit()