import pygame 
pygame.init()

def GetScreenSize():
    infoObject = pygame.display.Info()
    x = infoObject.current_w
    y = infoObject.current_h
    return x, y
