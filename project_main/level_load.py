import pygame
from init_img import ball

def LevelLoad(level, screen, LEVEL):
    if level == 1:
        LEVEL.draw(screen)
        ball.move()
