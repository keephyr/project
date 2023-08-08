import pygame
import init_img as ii
from threading import Event
import pygame_widgets
from pygame_widgets.slider import Slider
import importlib
from get_size import GetScreenSize
import resize_img

pygame.init()
event = Event()
main_screen = pygame.display.set_mode((0,0))
screen = main_screen.copy()
slider, textBox = ii.init_pygame_widget(main_screen, 1)
Widgets = (slider, textBox)
resize = True
scale = 1
screen_x, screen_y = GetScreenSize()
pygame.display.set_caption("Golf")
def Draw(action, clicked, run, event):
    global level, resize, main_screen, screen, slider, textBox, scale, screen_x, screen_y, Widgets
    if resize == True:
        x_s = screen_x * scale
        y_s = screen_y * scale
        screen = pygame.display.set_mode((x_s, y_s))
        importlib.reload(ii)
        importlib.reload(pygame_widgets)
        slider, textBox = resize_img.resize(scale, Widgets, x_s, y_s)
        # print(slider.set())
        # slider, textBox = ii.init_pygame_widget(main_screen, scale, slider, textBox)
        resize = False
    if action == "Start":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.START.draw(screen)
        for button in ii.START:
            if action != "Start":
                break
            else:
                level, action, clicked, resize = button.draw_clicked(action, clicked)
    elif action == "settings":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.SETTINGS.draw(screen)
        scale = ii.text_ScreenSize(textBox, slider)
        pygame_widgets.update(event)
        for button in ii.SETTINGS:
            if action != "settings":
                break
            else:
                level, action, clicked, resize = button.draw_clicked(action, clicked)
    elif action == "lvl_select":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.LVL_S.draw(screen)
        for button in ii.LVL_S:
            if action != "lvl_select":
                break
            else:
                level, action, clicked, resize = button.draw_clicked(action, clicked)
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
                    level, action, clicked, resize = img.draw_clicked(action, clicked)
    elif action == "pause":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.PAUSE.draw(screen)
        for button in ii.PAUSE:
            if action != "pause":
                break
            else:
                level, action, clicked, resize = button.draw_clicked(action, clicked)
    elif action == "exit":
        run = False
    else:
        run = False
        print("No action selected")
    main_screen.blit(pygame.transform.scale(screen, main_screen.get_rect().size), (0, 0))
    pygame.display.flip()
    return run, action, clicked


