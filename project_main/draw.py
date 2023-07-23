import pygame
from init_img import *
import level_load

pygame.init()

screen = pygame.display.set_mode((0,0))
pygame.display.set_caption("Golf")
def Draw(action, clicked, run):
    global level
    if action == "Start":
        BG.draw(screen)
        START.draw(screen)
        for button in START:
            level, action, clicked = button.draw_clicked(action, clicked)
    elif action == "settings":
        BG.draw(screen)
        SETTINGS.draw(screen)
        for button in SETTINGS:
            if action != "settings":
                break
            else:
                level, action, clicked = button.draw_clicked(action, clicked)
    elif action == "lvl_select":
        BG.draw(screen)
        LVL_S.draw(screen)
        for button in LVL_S:
            if action != "lvl_select":
                break
            else:
                level, action, clicked = button.draw_clicked(action, clicked)
    elif action == "level":
        clicked = False
        screen.blit(bg_image, (0,0))
        level_load.LevelLoad(level, screen, LEVEL)
    elif action == "exit":
        run = False
    else:
        run = False
        print("No action selected")
    pygame.display.flip()
    return run, action, clicked
