import pygame
import draw

clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    draw.Draw("Start")
    clock.tick(60)

pygame.quit()