import pygame
from os import path
from window_size import x, y

class Background(pygame.sprite.Sprite):
    def __init__(self, image):
        super().__init__()
        self.rect = image.get_rect() # rect - size of image 
        diff = self.difference(self.rect) # diff - difference between size of image and screen resolution
        self.image = pygame.transform.scale(image, (self.rect[2] * diff, self.rect[3] * diff)) # scaling image to the size of screen

    def difference(self, size):
        diff = x / size[2]
        return diff

    def get_size(self):
        x = self.image.get_rect()
        return x

images_dir = path.join(path.dirname(__file__), 'img')
bg_image = pygame.image.load(images_dir + "/Background/bg.png")
bg_image = Background(bg_image)
BG = pygame.sprite.Group()
BG.add(bg_image)
