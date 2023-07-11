import pygame
from init_img import BG
pygame.init()

screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
pygame.display.set_caption("Golf")

clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    BG.draw(screen)
    pygame.display.update()
    clock.tick(60)
pygame.quit()