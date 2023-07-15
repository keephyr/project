import pygame
from init_img import BG, START, LVL

pygame.init()

screen = pygame.display.set_mode((0,0))
pygame.display.set_caption("Golf")

def Draw(action, clicked, run):
    if action == "Start":
        BG.draw(screen)
        START.draw(screen)
        for button in START:
            action, clicked = button.draw_clicked(action, clicked)
    elif action == "lvl_select":
        BG.draw(screen)
        LVL.draw(screen)
        for button in LVL:
            action, clicked = button.draw_clicked(action, clicked)
    elif action == "exit":
        run = False
    pygame.display.update()
    return run, action, clicked
