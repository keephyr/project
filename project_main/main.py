import pygame
import draw

clicked = False
clock = pygame.time.Clock()
run = True
action = "Start"

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    run, action, clicked = draw.Draw(action, clicked, run)
    clock.tick(60)

pygame.quit()