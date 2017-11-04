import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (1024, 682)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
heads = True;

crashed = False

pygame.init()

while not crashed:

    from drawing import draw

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    screen.fill(WHITE)

    draw()

    pygame.display.update()

    clock.tick(60)
