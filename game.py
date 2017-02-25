import pygame

from engine.config import *
from game.game import Game

# initialize game engine
pygame.init()

# Load config
config = Config('resources/data/config.json')
# set screen width/height and caption

screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.name)

# initialize clock. used later in the loop.
clock = pygame.time.Clock()

# Initialize game
game = Game()
game.initialise()

# Game loop
done = False
while done == False:
    # write event handlers here
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    game.handle_input()
    game.update()

    screen.fill((100, 149, 237))
    game.render(screen)

    pygame.display.update()
    # run at 30 fps
    clock.tick(30)

pygame.quit()