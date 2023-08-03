import pygame
from init_img import ball

def LevelLoad(level, screen, BALL, event):
    while True:
        if event.is_set():
            break
        if level == 1:
            BALL.draw(screen)
            ball.move()
