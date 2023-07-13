import pygame
from os import path
from get_size import GetScreenSize

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
    
class Start(pygame.sprite.Sprite):
    def __init__(self, image, position, scale):
        super().__init__()
        size = image.get_rect()
        self.image = pygame.transform.scale(image, (size[2] * scale, size[3] * scale))
        self.rect = self.image.get_rect()
        self.rect.center = position

images_dir = path.join(path.dirname(__file__), 'img')

start_btn = pygame.image.load(images_dir + "/Buttons/start_notclicked.png") # Start Menu
settings_btn = pygame.image.load(images_dir + "/Buttons/set_notclicked.png")
exit_btn = pygame.image.load(images_dir + "/Buttons/exit_notclicked.png")
Name = pygame.image.load(images_dir + "/name.png")

start_btn = Start(start_btn, ((x_s/2),350), .4)
settings_btn = Start(settings_btn, ((x_s/2),500), .4)
exit_btn = Start(exit_btn, ((x_s/2),650), .4)
Name = Start(Name, ((x_s/2),150), 1.2)

START = pygame.sprite.Group()
START.add(start_btn, settings_btn, exit_btn, Name)

bg_image = pygame.image.load(images_dir + "/Background/bg.png") # Background
bg_toner = pygame.image.load(images_dir + "/Background/bg_toner.png")

bg_image = Background(bg_image)
bg_toner = Background(bg_toner)

BG = pygame.sprite.Group()
BG.add(bg_image)
BG.add(bg_toner)



