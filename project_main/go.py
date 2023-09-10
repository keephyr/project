import pygame
from get_size import GetScreenSize

clock = pygame.time.Clock()
clicked = False
pos1 = None
pos2 = None

def go(velx, vely, position, ball, Ball):
    from draw import screen, main_screen
    from init_img import bg_img, BALL, LEVEL, HOLE, INACTIVE
    x_s, y_s = GetScreenSize()
    x_vel = 1
    y_vel = 1
    number = 0.6
    goal = False
    outside_x = False
    outside_y = False
    while x_vel != 0 and y_vel != 0:
        i = 0
        x_vel = round(velx * number, 2)
        y_vel = round(vely * number, 2)
        position[0] = round(position[0] + round((x_vel * number) / 5, 3), 1)
        position[1] = round(position[1] + round((y_vel * number) / 5, 3), 1)

        if position[0] <= 0 or position[0] >= x_s:
            if outside_x == True:
                if position[0] > 0 or position[0] < x_s:
                    outside_x = False
                else:
                    pass
            else:
                x_vel = -x_vel      
                velx = -velx
                position[0] = round(position[0] + round((x_vel * number) / 10, 3), 1)
        if position[1] <= 0 or position[1] >= y_s:
            if outside_y == True:
                if position[1] > 0 or position[1] < y_s:
                    outside_y = False
                else:
                    pass
            else:
                y_vel = -y_vel      
                vely = -vely
                position[1] = round(position[1] + round((y_vel * number) / 10, 3), 1)

        ball.rect.center = position
        number = number - 0.01
        number = round(number,2)
        
        hit_list = pygame.sprite.spritecollide(ball, HOLE, False)
        for hit in hit_list:
            goal = True
        if goal == True:
            ball.rect.center = (-50,0)
            screen.blit(bg_img, (0,0))
            BALL.update()
            BALL.draw(screen)
            INACTIVE.draw(screen)
            # main_screen.blit(pygame.transform.scale(screen, main_screen.get_rect().size), (0, 0))
            pygame.display.flip()
            break
        screen.blit(bg_img, (0,0))
        BALL.update()
        # pause button
        # score
        # boxes
        HOLE.draw(screen)
        BALL.draw(screen)
        INACTIVE.draw(screen)
        # LEVEL.draw(screen)
        main_screen.blit(pygame.transform.scale(screen, main_screen.get_rect().size), (0, 0))
        pygame.display.flip()
    return goal

def clicked_func(ball, Ball):
    global clicked, pos1, pos2
    if pygame.mouse.get_pressed()[0] == True and clicked == False:
        clicked = True
        pos1 = pygame.mouse.get_pos()
        return False
    elif pygame.mouse.get_pressed()[0] == False and clicked == True:
        clicked = False
        pos2 = pygame.mouse.get_pos()
        goal = vel(pos1, pos2, ball, Ball)
        return goal

def vel(pos1, pos2, ball, Ball):
    velx = pos1[0] - pos2[0]
    vely = pos1[1] - pos2[1]
    position = list(ball.rect.center)
    goal = go(velx, vely, position,ball, Ball)
    return goal