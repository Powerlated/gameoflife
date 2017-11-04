import pygame
from pygame import transform

headsImg = pygame.image.load('resources/heads.jpg')
tailsImg = pygame.image.load('resources/tails.jpg')
guyImg = pygame.image.load('resources/guy.jpg')
sidewalkImg = pygame.image.load('resources/sidewalk.jpg')

def draw():
    __draw_background()
    __draw_guy()
    __draw_coin()

def __draw_background():
    from gameoflife import screen
    screen.blit(sidewalkImg, sidewalkImg.get_rect())


guy = pygame.sprite.Sprite()
guy.image = pygame.transform.scale(guyImg, (64, 64))
guy.rect = guyImg.get_rect()
group = pygame.sprite.GroupSingle(guy)


def __draw_guy():
    from gameoflife import screen

    group.draw(screen)


def __draw_coin():
    from gameoflife import screen, heads
    if heads:
        screen.blit(headsImg, headsImg.get_rect())
    else:
        screen.blit(tailsImg, tailsImg.get_rect())
