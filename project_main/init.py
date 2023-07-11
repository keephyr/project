import pygame
from os import path

images_dir = path.join(path.dirname(__file__), 'img')
image = pygame.image.load(path.join(images_dir, "hole.png")).convert()