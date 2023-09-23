import pygame
from os import path

from pygame.sprite import AbstractGroup
from get_size import GetScreenSize

import go
import change_action

x_s, y_s = GetScreenSize()
scale = x_s / 1920
print(scale)
class Background(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.rect = image.get_rect() # rect - size of image 
        diff = self.difference(self.rect) # diff - difference between size of image and screen resolution
        self.image = pygame.transform.scale(image, (self.rect[2] * diff, self.rect[3] * diff)) # scaling image to the size of screen

    def difference(self, size):
        diff = x_s / size[2]
        return diff

    def get_size(self):
        x = self.image.get_rect()
        return x
    
class Widget(pygame.sprite.Sprite):
    def __init__(self, image, position, scale, img_screen, img_class, level_num = None):
        super().__init__()
        self.level_num = level_num
        self.img_class = img_class
        self.img_screen = img_screen
        size = image.get_rect()
        self.new_size = (size[2] * scale, size[3] * scale)
        self.size = self.new_size
        self.image = pygame.transform.scale(image, self.new_size)
        if self.img_class == "ball" or self.img_class == "hole":
            self.image.set_colorkey([186,186,186])
        else:
            pass
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = position

    def draw_clicked(self,action, clicked,level_num = None, resize = False):
        
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and clicked == False:
                clicked = True
                if self.img_class != "name":
                    if self.img_screen == "main":
                        img_dir = buttons_dir + self.img_class + "_clicked.png"
                    elif self.img_screen == "lvl_select":
                        img_dir = level_btn_dir + self.img_class + "_clicked.png"
                    elif self.img_class == "pause_inactive":
                        img_dir = level_btn_dir + self.img_class
                    img_clicked = pygame.image.load(img_dir)
                    self.image = pygame.transform.scale(img_clicked, self.new_size)
            if pygame.mouse.get_pressed()[0] == False and clicked == True:
                clicked = False
                if self.img_class != "name":
                    if self.img_screen == "main":
                        img_dir = buttons_dir + self.img_class + "_notclicked.png"
                    elif self.img_screen == "lvl_select":
                        img_dir = level_btn_dir + self.img_class + "_notclicked.png"
                    elif self.img_class == "pause_inactive":
                        img_dir = level_btn_dir + self.img_class
                    img_notclicked = pygame.image.load(img_dir)
                    self.image = pygame.transform.scale(img_notclicked, self.new_size)
                if self.level_num != None:
                    self.level_num, action, resize = change_action.ChangeAction(action, self.img_class, self.level_num)
                else:
                    self.level_num, action, resize = change_action.ChangeAction(action, self.img_class, level_num)

        return self.level_num, action, clicked, resize
    
    def move(self):
        goal = go.clicked_func(self, Widget)
        return goal

    def Resize(self, scale):
        self.new_size = (self.size[0] * scale, self.size[1] * scale)      
        self.image = pygame.transform.scale(self.image, self.new_size)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        if self.img_class == "ball":
            self.image.set_colorkey([186,186,186])
        else:
            pass

class Box(pygame.sprite.Sprite):
    def __init__(self, image, position, scale):
        super().__init__()
        size = image.get_rect()
        self.position = position
        self.new_size = (size[2] * scale, size[3] * scale)
        self.size = self.new_size
        self.image = pygame.transform.scale(image, self.new_size)
        self.rect = self.image.get_rect()
        self.rect.center = position

images_dir = path.join(path.dirname(__file__), 'img/')
buttons_dir = path.join(path.dirname(__file__), 'img/Buttons/')
level_btn_dir = path.join(path.dirname(__file__), "img/Buttons/levels_buttons/")
text_dir = path.join(path.dirname(__file__), "img/Text/")
goal_frames = path.join(path.dirname(__file__), "img/Goal_anim/")
boxes_dir = path.join(path.dirname(__file__), 'img/Boxes/')

ANIM_FRAMES = pygame.sprite.Group()



start_btn_img = pygame.image.load(buttons_dir + "start_notclicked.png") # Start Menu
set_btn_img = pygame.image.load(buttons_dir + "set_notclicked.png")
exit_btn_img = pygame.image.load(buttons_dir + "exit_notclicked.png")
Name_img = pygame.image.load(images_dir + "name.png")

start_btn = Widget(start_btn_img, ((x_s/2),((y_s/20) * 8)), .4 * scale,"main", "start")
set_btn = Widget(set_btn_img, ((x_s/2),((y_s/20) * 11)), .4 * scale,"main", "set")
exit_btn = Widget(exit_btn_img, ((x_s/2),((y_s/20) * 14)), .4 * scale,"main", "exit")
Name = Widget(Name_img, ((x_s/2),(y_s/7)), 1.2 * scale, "main", "name")

START = pygame.sprite.Group()
START.add(start_btn, set_btn, exit_btn, Name)



bg_img = pygame.image.load(images_dir + "Background/bg.png") # Background
bg_toner_img = pygame.image.load(images_dir + "Background/bg_toner.png")

bg = Background(bg_img)
bg_toner = Background(bg_toner_img)

BG = pygame.sprite.Group()

BG.add(bg_toner)



back_btn_img = pygame.image.load(level_btn_dir + "back_notclicked.png") # Level select
N1_btn_img = pygame.image.load(level_btn_dir + "N1_notclicked.png")
N2_btn_img = pygame.image.load(level_btn_dir + "N2_notclicked.png")
N3_btn_img = pygame.image.load(level_btn_dir + "N3_notclicked.png")
N4_btn_img = pygame.image.load(level_btn_dir + "N4_notclicked.png")
N5_btn_img = pygame.image.load(level_btn_dir + "N5_notclicked.png")
N6_btn_img = pygame.image.load(level_btn_dir + "N6_notclicked.png")
Level_select_Name_img = pygame.image.load(level_btn_dir + "level_select.png")

back_btn = Widget(back_btn_img, ((x_s/5),(y_s/10)), .3 * scale, "lvl_select", "back")

N1_btn = Widget(N1_btn_img, (((x_s/2) - (x_s/10)),((y_s/10) * 3)), .3 * scale, "lvl_select", "N1", 1) # x pos - (x_s/2) +- (x_s/10)
N2_btn = Widget(N2_btn_img, (((x_s/2))          ,((y_s/10) * 3)), .3 * scale, "lvl_select", "N2", 2)  # y pos - y_s/10 * 3/5/7
N3_btn = Widget(N3_btn_img, (((x_s/2) + (x_s/10)),((y_s/10) * 3)), .3 * scale, "lvl_select", "N3", 3)
N4_btn = Widget(N4_btn_img, (((x_s/2) - (x_s/10)),((y_s/10) * 5)), .3 * scale, "lvl_select", "N4", 4) # x pos - (x_s/2) +- (x_s/10)
N5_btn = Widget(N5_btn_img, (((x_s/2))          ,((y_s/10) * 5)), .3 * scale, "lvl_select", "N5", 5)  # y pos - y_s/10 * 3/5/7
N6_btn = Widget(N6_btn_img, (((x_s/2) + (x_s/10)),((y_s/10) * 5)), .3 * scale, "lvl_select", "N6", 6)

Level_select_Name = Widget(Level_select_Name_img,(((x_s/2)),(y_s/10)), .9 * scale, "lvl_select", "name")

LVL_S = pygame.sprite.Group()
LVL_S.add(back_btn, N1_btn, N2_btn, N3_btn,N4_btn,N5_btn,N6_btn, Level_select_Name)



ball_img = pygame.image.load(images_dir + "ball.png")
pause_btn_img = pygame.image.load(level_btn_dir + "pause_notclicked.png")
pause_inactve_img = pygame.image.load(level_btn_dir + "pause_inactive.png")
hole_img = pygame.image.load(images_dir + "hole.png")

next_level_img = pygame.image.load(level_btn_dir + "next_notclicked.png")
level_passed_img = pygame.image.load(text_dir + "level_passed.png")

ball = Widget(ball_img, ((x_s/2), (y_s - y_s / 6)), .2 * scale, "level", "ball")
pause_btn = Widget(pause_btn_img, ((y_s/15),(y_s/15)), .25 * scale, "lvl_select", "pause")
pause_inactve = Widget(pause_inactve_img, ((y_s/15),(y_s/15)), .25 * scale, "lvl_select", "pause_inactive")
hole = Widget(hole_img, ((x_s/2), (y_s/6)), .4 * scale, "level", "hole")

level_passed = Widget(level_passed_img, ((x_s/2),(y_s/7)), 1.2 * scale, "main", "name")
next_level = Widget(next_level_img, ((x_s/2),((y_s/10) * 8)), .3 * scale, "lvl_select", "next")

LEVEL = pygame.sprite.Group()
BALL = pygame.sprite.Group()
HOLE = pygame.sprite.Group()
INACTIVE = pygame.sprite.Group()
LEVEL_BUTTONS = pygame.sprite.Group()

HOLE.add(hole)
BALL.add(ball)
LEVEL.add(hole, ball, pause_btn)
LEVEL_BUTTONS.add(pause_btn, next_level, level_passed)
INACTIVE.add(pause_inactve)



res_img = pygame.image.load(text_dir + "resolution.png")

res = Widget(res_img, ((x_s/4),((y_s/10) * 3)), .6 * scale, "res_select", "name")

apply_img = pygame.image.load(buttons_dir + "apply_notclicked.png")

apply = Widget(apply_img, ((x_s/2),((y_s/10) * 8)), .3 * scale, "main", "apply")

SETTINGS = pygame.sprite.Group()
SETTINGS.add(res, back_btn, apply)



resume_btn_img = pygame.image.load(buttons_dir + "res_notclicked.png")
resume_btn = Widget(resume_btn_img, ((x_s/2),(y_s/20) * 8), .4 * scale, "main", "res")

pause_img = pygame.image.load(text_dir + "pause.png")
pause = Widget(pause_img, ((x_s/2),(y_s/7)), 1.2 * scale, "pause", "name")

PAUSE = pygame.sprite.Group()
PAUSE.add(resume_btn, set_btn, exit_btn, pause)



box_img = pygame.image.load(boxes_dir + "box.png")
box_2_col_img = pygame.image.load(boxes_dir + "boxes_2_column.png")
box_3_row_img = pygame.image.load(boxes_dir + "boxes_3_row.png")
box_5_row_img = pygame.image.load(boxes_dir + "boxes_5_row.png")

box = Box(box_img, (-50,-50), 2)
box_2_col = Box(box_2_col_img, (-50,-50), 2)
box_3_row = Box(box_3_row_img, (-50,-50), 2)
box_5_row = Box(box_5_row_img, (-50,-50), 2)

BOXES = pygame.sprite.Group()

BOXES.add(box, box_2_col, box_5_row, box_3_row)


