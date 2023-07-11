import pygame

pygame.init()

screenWidth = 1920
screenHeight = 1080

screen = pygame.display.set_mode((0,0), pygame.RESIZABLE)
pygame.display.set_caption("Golf")

clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.flip()
    

pygame.quit()