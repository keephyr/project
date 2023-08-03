import pygame
import init_img as ii
from threading import Event
import importlib
import resize_img

pygame.init()
event = Event()
main_screen = pygame.display.set_mode((0,0))
screen = main_screen.copy()
resize = True
pygame.display.set_caption("Golf")
def Draw(action, clicked, run):
    global level, resize, main_screen, screen
    if action == "Start":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.START.draw(screen)
        for button in ii.START:
            level, action, clicked = button.draw_clicked(action, clicked)
    elif action == "settings":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.SETTINGS.draw(screen)
        for button in ii.SETTINGS:
            if action != "settings":
                break
            else:
                level, action, clicked = button.draw_clicked(action, clicked)
    elif action == "lvl_select":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.LVL_S.draw(screen)
        for button in ii.LVL_S:
            if action != "lvl_select":
                break
            else:
                level, action, clicked = button.draw_clicked(action, clicked)
    elif action == "level":
        screen.blit(ii.bg_img, (0,0))
        ii.LEVEL.draw(screen)
        for img in ii.LEVEL:
            if action != "level":
                break
            else:
                if img.img_class == "ball":
                    img.move()
                else:
                    level, action, clicked = img.draw_clicked(action, clicked)
    elif action == "pause":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.PAUSE.draw(screen)
        for button in ii.PAUSE:
            if action != "pause":
                break
            else:
                level, action, clicked = button.draw_clicked(action, clicked)
    elif action == "exit":
        run = False
    else:
        run = False
        print("No action selected")
    if resize == True:
        scale = .5
        x_s = ii.x_s * scale
        y_s = ii.y_s * scale
        screen = pygame.display.set_mode((x_s, y_s))
        importlib.reload(ii)
        resize_img.resize(scale)
        resize = False
    main_screen.blit(pygame.transform.scale(screen, main_screen.get_rect().size), (0, 0))
    pygame.display.flip()
    return run, action, clicked


