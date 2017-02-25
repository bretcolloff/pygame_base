import pygame

from engine.config import *
from game.game import Game

# initialize pygame.
pygame.init()
pygame.font.init()

# Load config and set window parameters.
config = Config('resources/data/config.json')
screen = pygame.display.set_mode((config.width, config.height))
pygame.display.set_caption(config.name)

# initialize clock.
clock = pygame.time.Clock()

# Load in a font.
font = pygame.font.SysFont("Comic Sans MS", 30)

# Initialize game.
game = Game(config, clock)
game.initialise('resources/data/data.json')

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
    game.render(screen, font)

    pygame.display.update()

pygame.quit()
