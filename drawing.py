import pygame
from gameoflife import screen
import gameoflife as g


def draw():
    __draw_background()


def __draw_background():
    screen.blit(g.sidewalkImg, 1, 1)
