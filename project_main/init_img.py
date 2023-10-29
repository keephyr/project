import pygame
from os import path

from get_size import GetScreenSize

import go
import change_action

x_s, y_s = GetScreenSize()
scale = x_s / 1920
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
    def __init__(self, image, position, scale, img_screen, img_class, level_num = None, biome = None):
        super().__init__()
        self.biome = biome
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

    def draw_clicked(self,action, clicked,biome_num,level_num = None, resize = False):
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
                    self.level_num, action, resize, biome_num = change_action.ChangeAction(action, self.img_class, biome_num, self.level_num)
                else:
                    self.level_num, action, resize, biome_num = change_action.ChangeAction(action, self.img_class, biome_num, level_num)

        return self.level_num, action, clicked, resize, biome_num
    
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

class Prop(pygame.sprite.Sprite):
    def __init__(self, image, position, scale, prop_class):
        super().__init__()
        self.prop_class = prop_class
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
props_dir = path.join(path.dirname(__file__), 'img/Props/')

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



bg_plain_img = pygame.image.load(images_dir + "Background/bg_plain.png") # Background
bg_plain_img = pygame.transform.scale(bg_plain_img, (1000 * (1 + scale), 1000 * (1 + scale)))
bg_sand_img = pygame.image.load(images_dir + "Background/bg_sand.png")
bg_sand_img = pygame.transform.scale(bg_sand_img, (1000 * (1 + scale), 1000 * (1 + scale)))
bg_toner_img = pygame.image.load(images_dir + "Background/bg_toner.png")
bg_ice_img = pygame.image.load(images_dir + "Background/bg_ice.png")
bg_ice_img = pygame.transform.scale(bg_ice_img, (1000 * (1 + scale), 1000 * (1 + scale)))

bg_img = bg_plain_img
# bg = Background(bg_sand_img)
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
N7_btn_img = pygame.image.load(level_btn_dir + "N7_notclicked.png")
N8_btn_img = pygame.image.load(level_btn_dir + "N8_notclicked.png")
N9_btn_img = pygame.image.load(level_btn_dir + "N9_notclicked.png")
N10_btn_img = pygame.image.load(level_btn_dir + "N10_notclicked.png")
N11_btn_img = pygame.image.load(level_btn_dir + "N11_notclicked.png")


Plain_img = pygame.image.load(text_dir + "Plain.png")
Sand_img = pygame.image.load(text_dir + "Sand.png")
Ice_img = pygame.image.load(text_dir + "Ice.png")

left_btn_img = pygame.image.load(level_btn_dir + "left_notclicked.png")
right_btn_img = pygame.image.load(level_btn_dir + "right_notclicked.png")

back_btn = Widget(back_btn_img, ((x_s/5),(y_s/10)), .3 * scale, "lvl_select", "back")

N1_btn = Widget(N1_btn_img, (((x_s/2) - (x_s/10)),((y_s/10) * 3)), .3 * scale, "lvl_select", "N1", 1, biome = "plain") # x pos - (x_s/2) +- (x_s/10)
N2_btn = Widget(N2_btn_img, (((x_s/2))          ,((y_s/10) * 3)), .3 * scale, "lvl_select", "N2", 2, biome = "plain")  # y pos - y_s/10 * 3/5/7
N3_btn = Widget(N3_btn_img, (((x_s/2) + (x_s/10)),((y_s/10) * 3)), .3 * scale, "lvl_select", "N3", 3, biome = "plain")

N4_btn = Widget(N4_btn_img, (((x_s/2) - (x_s/10)),((y_s/10) * 5)), .3 * scale, "lvl_select", "N4", 4, biome = "plain") # x pos - (x_s/2) +- (x_s/10)
N5_btn = Widget(N5_btn_img, (((x_s/2))          ,((y_s/10) * 5)), .3 * scale, "lvl_select", "N5", 5, biome = "plain")  # y pos - y_s/10 * 3/5/7
N6_btn = Widget(N6_btn_img, (((x_s/2) + (x_s/10)),((y_s/10) * 5)), .3 * scale, "lvl_select", "N6", 6, biome = "plain")

N7_btn = Widget(N7_btn_img, (((x_s/2) - (x_s/10)),((y_s/10) * 7)), .3 * scale, "lvl_select", "N7", 7, biome = "plain")
N8_btn = Widget(N8_btn_img, (((x_s/2))           ,((y_s/10) * 7)), .3 * scale, "lvl_select", "8", 8, biome = "plain")
N9_btn = Widget(N9_btn_img, (((x_s/2) + (x_s/10)),((y_s/10) * 7)), .3 * scale, "lvl_select", "9", 9, biome = "plain")

N10_btn = Widget(N10_btn_img, (((x_s/2))          ,((y_s/10) * 9)), .3 * scale, "lvl_select", "N10", 10, biome = "plain") # PLAIN BIOME

N11_btn = Widget(N11_btn_img, (((x_s/2) - (x_s/10)),((y_s/10) * 3)), .3 * scale, "lvl_select", "N11", 11, biome = "sand")

left_btn = Widget(left_btn_img,((x_s/5),y_s - (y_s/10)), .3 * scale, "lvl_select", "left")
right_btn = Widget(right_btn_img,(x_s - (x_s/5),y_s - (y_s/10)), .3 * scale, "lvl_select", "right")

Plain_name = Widget(Plain_img,(((x_s/2)),(y_s/10)), .9 * scale, "lvl_select", "name")
Sand_name = Widget(Sand_img,(((x_s/2)),(y_s/10)), .9 * scale, "lvl_select", "name")
Ice_name = Widget(Ice_img,(((x_s/2)),(y_s/10)), .9 * scale, "lvl_select", "name")

LVL_S = pygame.sprite.Group()
PLAIN = pygame.sprite.Group()
SAND = pygame.sprite.Group()
ICE = pygame.sprite.Group()
BTNS = pygame.sprite.Group()

LVL_S.add(back_btn, left_btn, right_btn)
PLAIN.add(Plain_name, N1_btn, N2_btn, N3_btn, N4_btn, N5_btn, N6_btn, N7_btn, N8_btn, N9_btn, N10_btn)
SAND.add(Sand_name, N11_btn)
ICE.add(Ice_name)

buttons = [N1_btn, N2_btn, N3_btn, N4_btn, N5_btn, N6_btn, N7_btn, N8_btn, N9_btn, N10_btn, N11_btn]
BTNS.add(back_btn, left_btn, right_btn, N1_btn, N2_btn, N3_btn, N4_btn, N5_btn, N6_btn, N7_btn, N8_btn, N9_btn, N10_btn, N11_btn)


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



box_img = pygame.image.load(props_dir + "box.png")
box_2_col_img = pygame.image.load(props_dir + "boxes_2_column.png")
box_3_row_img = pygame.image.load(props_dir + "boxes_3_row.png")
box_5_row_img = pygame.image.load(props_dir + "boxes_5_row.png")

sand_prop_img = pygame.image.load(props_dir + "sand_prop.png")
ice_prop_img = pygame.image.load(props_dir + "ice_prop.png")

box1=box2=box3=box4=box5=box6=box7=box8= Prop(box_img, (-50,-50), 4, "box")
box_2_col = Prop(box_2_col_img, (-50,-50), 2, "box")
box_3_row = Prop(box_3_row_img, (-50,-50), 2, "box")
box_5_row = Prop(box_5_row_img, (-50,-50), 2, "box")

sand_prop = Prop(sand_prop_img, (-50,-50), .4, "sand")
ice_prop = Prop(ice_prop_img, (-50,-50), .4, "ice")

PROPS = pygame.sprite.Group()
SAND_PROP = pygame.sprite.Group()
ICE_PROP = pygame.sprite.Group()
box_array = [box1,box2,box3,box4,box5,box6,box7,box8]
PROPS.add(box1,box2,box3,box4,box5,box6,box7,box8, box_2_col, box_5_row, box_3_row, sand_prop, ice_prop)
SAND_PROP.add(sand_prop)
ICE_PROP.add(ice_prop)

map1 = [[0,1,0,0,0,0,0,0],
       [1,0,1,0,0,0,0,0],
       [0,1,0,0,0,0,0,0],
       [1,0,1,0,0,0,0,0]]