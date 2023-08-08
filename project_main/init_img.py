import pygame
from os import path
from get_size import GetScreenSize

import go
import change_action

x_s, y_s = GetScreenSize()

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
        if self.img_class == "ball":
            self.image.set_colorkey([186,186,186])
        else:
            pass
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.position = position

    def draw_clicked(self,action, clicked, resize = False):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == True and clicked == False:
                clicked = True
                if self.img_class != "name":
                    if self.img_screen == "main":
                        img_dir = buttons_dir + self.img_class + "_clicked.png"
                    elif self.img_screen == "lvl_select":
                        img_dir = level_btn_dir + self.img_class + "_clicked.png"
                    img_clicked = pygame.image.load(img_dir)
                    self.image = pygame.transform.scale(img_clicked, self.new_size)
            if pygame.mouse.get_pressed()[0] == False and clicked == True:
                clicked = False
                if self.img_class != "name":
                    if self.img_screen == "main":
                        img_dir = buttons_dir + self.img_class + "_notclicked.png"
                    elif self.img_screen == "lvl_select":
                        img_dir = level_btn_dir + self.img_class + "_notclicked.png"
                    img_notclicked = pygame.image.load(img_dir)
                    self.image = pygame.transform.scale(img_notclicked, self.new_size)
                self.level_num, action, resize = change_action.ChangeAction(action, self.img_class, self.level_num)

        return self.level_num, action, clicked, resize
    
    def move(self):
        go.clicked_func(self, Widget)

    def Resize(self, scale):
        self.new_size = (self.size[0] * scale, self.size[1] * scale)      
        self.image = pygame.transform.scale(self.image, self.new_size)
        self.rect = self.image.get_rect()
        self.rect.center = self.position
        if self.img_class == "ball":
            self.image.set_colorkey([186,186,186])
        else:
            pass

images_dir = path.join(path.dirname(__file__), 'img/')
buttons_dir = path.join(path.dirname(__file__), 'img/Buttons/')
level_btn_dir = path.join(path.dirname(__file__), "img/Buttons/levels_buttons/")
text_dir = path.join(path.dirname(__file__), "img/Text/")

start_btn_img = pygame.image.load(buttons_dir + "start_notclicked.png") # Start Menu
set_btn_img = pygame.image.load(buttons_dir + "set_notclicked.png")
exit_btn_img = pygame.image.load(buttons_dir + "exit_notclicked.png")
Name_img = pygame.image.load(images_dir + "name.png")

start_btn = Widget(start_btn_img, ((x_s/2),((y_s/20) * 8)), .4,"main", "start")
set_btn = Widget(set_btn_img, ((x_s/2),((y_s/20) * 11)), .4,"main", "set")
exit_btn = Widget(exit_btn_img, ((x_s/2),((y_s/20) * 14)), .4,"main", "exit")
Name = Widget(Name_img, ((x_s/2),(y_s/7)), 1.2,"main", "name")

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
Level_select_Name_img = pygame.image.load(level_btn_dir + "level_select.png")

back_btn = Widget(back_btn_img, ((x_s/5),(y_s/10)), .3, "lvl_select", "back")

N1_btn = Widget(N1_btn_img, (((x_s/2) - (x_s/10)),((y_s/10) * 3)), .3, "lvl_select", "N1", 1) # x pos - (x_s/2) +- (x_s/10)
N2_btn = Widget(N2_btn_img, (((x_s/2))          ,((y_s/10) * 3)), .3, "lvl_select", "N2", 2)  # y pos - y_s/10 * 3/5/7
N3_btn = Widget(N3_btn_img, (((x_s/2) + (x_s/10)),((y_s/10) * 3)), .3, "lvl_select", "N3", 3)

Level_select_Name = Widget(Level_select_Name_img,(((x_s/2)),(y_s/10)), .9, "lvl_select", "name")

LVL_S = pygame.sprite.Group()
LVL_S.add(back_btn, N1_btn, N2_btn, N3_btn, Level_select_Name)

ball_img = pygame.image.load(images_dir + "ball.png")
pause_btn_img = pygame.image.load(level_btn_dir + "pause_notclicked.png")

ball = Widget(ball_img, ((x_s/2), (y_s/2)), .2, "level", "ball")
pause_btn = Widget(pause_btn_img, ((y_s/15),(y_s/15)), .25, "lvl_select", "pause")

LEVEL = pygame.sprite.Group()
BALL = pygame.sprite.Group()
BALL.add(ball)
LEVEL.add(ball, pause_btn)

res_img = pygame.image.load(text_dir + "resolution.png")

res = Widget(res_img, ((x_s/4),((y_s/10) * 3)), .6, "res_select", "name")

apply_img = pygame.image.load(buttons_dir + "apply_notclicked.png")

apply = Widget(apply_img, ((x_s/2),((y_s/10) * 8)), .3, "main", "apply")

SETTINGS = pygame.sprite.Group()
SETTINGS.add(res, back_btn, apply)

resume_btn_img = pygame.image.load(buttons_dir + "res_notclicked.png")
resume_btn = Widget(resume_btn_img, ((x_s/2),(y_s/20) * 8), .4, "main", "res")

pause_img = pygame.image.load(text_dir + "pause.png")
pause = Widget(pause_img, ((x_s/2),(y_s/7)), 1.2, "pause", "name")

PAUSE = pygame.sprite.Group()
PAUSE.add(resume_btn, set_btn, exit_btn, pause)

# dictionary = locals()
# variable = 2
# char = None
# for variable in dictionary.items():
#     print(variable[1])
#     variable[1].replace()
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox    
def init_pygame_widget(screen, scale, slider = None, textBox = None):
    global x_s, y_s, Slider, TextBox

    slider = Slider(screen, int(x_s/2.3),int(((y_s/10) * 2.7)),400,50, min=10, max=100, step=10, initial=100, colour=(242, 196, 116), handleColour=(46, 45, 6))
    textBox = TextBox(screen, int(x_s/1.3),int(((y_s/10) * 2.7)),200,50, fontSize=40, radius = 5, colour=(242, 196, 116), textColour=(46, 45, 6))
    textBox.disable()
    # slider = Slider(screen, 20,10,400,50)
    print(slider._y)
    

    return slider, textBox

def text_ScreenSize(textBox, slider):
    screen_x, screen_y = GetScreenSize()

    Value = slider.getValue()
    Value = (Value / 100)

    screen_size = (str(int(screen_x * Value)) + " x " + str(int(screen_y * Value)))

    textBox.setText(screen_size)

    return Value
