import pygame

from engine.config import *
from game.game import Game

# initialize pygame
pygame.init()

# Load config and set window parameters.
config = Config('resources/data/config.json')
screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.name)

# initialize clock.
clock = pygame.time.Clock()

# Initialize game
game = Game(config, clock)
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

pygame.quit()
