# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

import pygame
size = (700, 500)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

headsImg = pygame.image.load('heads.jpg')
tailsImg = pygame.image.load('tails.jpg')
guyImg = pygame.image.load('guy.jpg')
sidewalkImg = pygame.image.load('sidewalk.jpg')



crashed = False

while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    screen.fill(WHITE)

    pygame.display.update()
    clock.tick(60)

