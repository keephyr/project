import pygame
import draw
from draw import screen, main_screen

clicked = False
clock = pygame.time.Clock()
run = True
action = "Start"

while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
    run, action, clicked = draw.Draw(action, clicked, run, events)
    clock.tick(60)

pygame.quit()