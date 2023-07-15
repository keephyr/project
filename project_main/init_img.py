import pygame
from os import path
from get_size import GetScreenSize
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
    def __init__(self, image, position, scale, img_screen, img_class):
        super().__init__()
        self.img_class = img_class
        self.img_screen = img_screen
        size = image.get_rect()
        self.new_size = (size[2] * scale, size[3] * scale)
        self.image = pygame.transform.scale(image, self.new_size)
        self.rect = self.image.get_rect()
        self.rect.center = position

    def draw_clicked(self,action, clicked):
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
                action = change_action.ChangeAction(action, self.img_class)
                
        return action, clicked

images_dir = path.join(path.dirname(__file__), 'img')
buttons_dir = path.join(path.dirname(__file__), 'img/Buttons/')
level_btn_dir = path.join(path.dirname(__file__), "img/Buttons/levels_buttons/")

start_btn = pygame.image.load(images_dir + "/Buttons/start_notclicked.png") # Start Menu
set_btn = pygame.image.load(images_dir + "/Buttons/set_notclicked.png")
exit_btn = pygame.image.load(images_dir + "/Buttons/exit_notclicked.png")
Name = pygame.image.load(images_dir + "/name.png")

Buttons = []
Buttons.append(start_btn)

start_btn = Widget(start_btn, ((x_s/2),350), .4,"main", "start")
set_btn = Widget(set_btn, ((x_s/2),500), .4,"main", "set")
exit_btn = Widget(exit_btn, ((x_s/2),650), .4,"main", "exit")
Name = Widget(Name, ((x_s/2),150), 1.2,"main", "name")

START = pygame.sprite.Group()
START.add(start_btn, set_btn, exit_btn, Name)

bg_image = pygame.image.load(images_dir + "/Background/bg.png") # Background
bg_toner = pygame.image.load(images_dir + "/Background/bg_toner.png")

bg_image = Background(bg_image)
bg_toner = Background(bg_toner)

BG = pygame.sprite.Group()
BG.add(bg_image)
BG.add(bg_toner)

back_btn = pygame.image.load(level_btn_dir + "back_notclicked.png") # Level select
N1_btn = pygame.image.load(level_btn_dir + "N1_notclicked.png")
N2_btn = pygame.image.load(level_btn_dir + "N2_notclicked.png")
N3_btn = pygame.image.load(level_btn_dir + "N3_notclicked.png")
Level_select_Name = pygame.image.load(level_btn_dir + "level_select.png")

back_btn = Widget(back_btn, ((x_s/5),(y_s/10)), .3, "lvl_select", "back")

N1_btn = Widget(N1_btn, (((x_s/2) - (x_s/10)),((y_s/10) * 3)), .3, "lvl_select", "N1") # x pos - (x_s/2) +- (x_s/10)
N2_btn = Widget(N2_btn, (((x_s/2))          ,((y_s/10) * 3)), .3, "lvl_select", "N2")  # y pos - y_s/10 * 3/5/7
N3_btn = Widget(N3_btn, (((x_s/2) + (x_s/10)),((y_s/10) * 3)), .3, "lvl_select", "N3")

Level_select_Name = Widget(Level_select_Name,(((x_s/2)),(y_s/10)), .9, "lvl_select", "name")

LVL = pygame.sprite.Group()
LVL.add(back_btn, N1_btn, N2_btn, N3_btn, Level_select_Name)


