import pygame
import init_img as ii
import importlib

from get_size import GetScreenSize
from level_load import LevelLoad
from change_pos import Change_btn_pos

pygame.init()
main_screen = pygame.display.set_mode((960,540))
screen = main_screen.copy()
resize = True
scale = 1
level_num = None
loading = False
screen_x, screen_y = GetScreenSize()
biome = 0
pygame.display.set_caption("Golf")
clock = pygame.time.Clock()

def Draw(action, clicked, run):
    global resize, main_screen, screen, scale, screen_x, screen_y, clock, level_num, loading, biome
    if resize == True:
        x_s = screen_x * scale
        y_s = screen_y * scale
        screen = pygame.display.set_mode((x_s, y_s))
        importlib.reload(ii)
        resize = False
    if action == "Start":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.START.draw(screen)
        for button in ii.START:
            level, action, clicked, resize, biome = button.draw_clicked(action, clicked, biome, level_num)              
            if action != "Start":
                break
    elif action == "settings":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.SETTINGS.draw(screen)
        for button in ii.SETTINGS:
            level, action, clicked, resize, biome = button.draw_clicked(action, clicked, biome, level_num)  
            if action != "settings":
                break                      
    elif action == "lvl_select":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.LVL_S.draw(screen)
        ii.BTNS, ii.PLAIN, ii.SAND = Change_btn_pos(biome)
        if biome == 0:
            ii.bg_img = ii.bg_plain_img
            ii.PLAIN.draw(screen)
        elif biome == 1:
            ii.bg_img = ii.bg_sand_img
            ii.SAND.draw(screen)
        loading = True
        for button in ii.BTNS:
            level, action, clicked, resize, biome = button.draw_clicked(action, clicked, biome, level_num)
            if level != None:
                level_num = level
            if action != "lvl_select":
                if action == "level":
                    loading, level_num = LevelLoad(level_num, screen, action, loading = loading) 
                break              
    elif action == "level":
        screen.blit(ii.bg_img, (0,0))
        loading, level_num = LevelLoad(level_num, screen, action)
        num = 0
        for img in ii.LEVEL:
            level, action, clicked, resize, biome = img.draw_clicked(action, clicked, biome, level_num)                   
            if action != "level":
                break
            else:
                if img.img_class == "ball":
                    goal = img.move()
                    if goal == True:
                        loading = True
                        while num < 20:
                            clock.tick(20)
                            screen.blit(ii.bg_img, (0,0))
                            LevelLoad(level_num, screen, "action")
                            anim_image = pygame.image.load(ii.goal_frames + f"pixil-frame-{num}.png")
                            anim_image = ii.Widget(anim_image, ((ii.x_s/2), (ii.y_s/6)), .4 * ii.scale, "level", "hole")
                            ii.ANIM_FRAMES.add(anim_image)
                            ii.ANIM_FRAMES.draw(screen)
                            num = num + 1
                            anim_image = {}
                            pygame.display.flip()
                        clock.tick(60)
                        action = "next_level"
    elif action == "pause":
        screen.blit(ii.bg_img, (0,0))
        ii.BG.draw(screen)
        ii.PAUSE.draw(screen)
        for button in ii.PAUSE:
            level, action, clicked, resize, biome = button.draw_clicked(action, clicked, biome, level_num)
            if action != "pause":
                break
    elif action == "next_level":
        screen.blit(ii.bg_img, (0,0))
        loading, level_num = LevelLoad(level_num, screen, action, loading)
        ii.LEVEL_BUTTONS.draw(screen)
        for button in ii.LEVEL_BUTTONS:
            level, action, clicked, resize, biome = button.draw_clicked(action, clicked, biome, level_num)
            if action != "next_level":
                level_num = level_num + 1
                loading, level_num = LevelLoad(level_num, screen, action, loading)
                break
    elif action == "exit":
        run = False
    else:
        run = False
        print("No action selected")
    main_screen.blit(pygame.transform.scale(screen, main_screen.get_rect().size), (0, 0))
    pygame.display.flip()
    return run, action, clicked


