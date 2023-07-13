import pygame
from init_img import BG, START
pygame.init()

screen = pygame.display.set_mode((0,0))
pygame.display.set_caption("Golf")

def Draw(action):
    if action == "Start":
        BG.draw(screen)
        START.draw(screen)
    
    pygame.display.update()