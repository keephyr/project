import pygame 
pygame.init()

infoObject = pygame.display.Info()
x = infoObject.current_w
y = infoObject.current_h

if __name__ == "__main__":
    print(type(x))