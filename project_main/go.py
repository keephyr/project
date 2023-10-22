import pygame
from get_size import GetScreenSize

clock = pygame.time.Clock()
clicked = False
pos1 = None
pos2 = None

def go(velx, vely, position, ball, Ball):
    from level_load import LevelLoad
    from draw import screen, main_screen, level_num, screen
    from init_img import bg_img, BALL, LEVEL, HOLE, INACTIVE, PROPS
    x_s, y_s = GetScreenSize()
    x_vel = 1
    y_vel = 1
    number = .9
    goal = False
    while x_vel != 0 and y_vel != 0:
        x_vel = round(velx * number, 2)
        y_vel = round(vely * number, 2)

        hit_list = pygame.sprite.spritecollide(ball, PROPS, False)
        if len(hit_list) != 0:
            for box in hit_list:
                if box.prop_class == "box":
                    if ball.rect.right >= box.rect.left and ball.rect.left < box.rect.left: #left side of the box
                        if ball.rect.top >= box.rect.top and ball.rect.bottom <= box.rect.bottom:
                                x_vel = -abs(x_vel)
                                velx = -abs(velx)
                                position[0] = round(position[0] + round((x_vel * number) / 20, 3), 1)
                    if ball.rect.left <= box.rect.right and ball.rect.right > box.rect.right: # right side of the box
                        if ball.rect.top >= box.rect.top and ball.rect.bottom <= box.rect.bottom:
                                x_vel = abs(x_vel)
                                velx = abs(velx)
                                position[0] = round(position[0] + round((x_vel * number) / 20, 3), 1)
                    if ball.rect.top <= box.rect.bottom and ball.rect.bottom > box.rect.bottom: # bottom side of the box
                        if ball.rect.left >= box.rect.left and ball.rect.right <= box.rect.right:
                                y_vel = abs(y_vel)
                                vely = abs(vely)
                                position[1] = round(position[1] + round((y_vel * number) / 20, 3), 1)
                    if ball.rect.bottom >= box.rect.top and ball.rect.top < box.rect.top: # bottom side of the box
                        if ball.rect.left >= box.rect.left and ball.rect.right <= box.rect.right:
                                y_vel = -abs(y_vel)
                                vely = -abs(vely)
                                position[1] = round(position[1] + round((y_vel * number) / 20, 3), 1)
                elif box.prop_class == "sand":
                    position[0] = round(position[0] + round((x_vel * number) / 20, 3), 1)
                    position[1] = round(position[1] + round((y_vel * number) / 20, 3), 1)
                    number = number - 0.05
                    if number < 0:
                        number = 0
                    number = round(number,2)
                if box.prop_class != "sand":
                    position[0] = round(position[0] + round((x_vel * number) / 20, 3), 1)
                    position[1] = round(position[1] + round((y_vel * number) / 20, 3), 1)
                    number = number - 0.02
                    number = round(number,2)
        else:
            position[0] = round(position[0] + round((x_vel * number) / 20, 3), 1)
            position[1] = round(position[1] + round((y_vel * number) / 20, 3), 1)
            number = number - 0.01
            number = round(number,2)
                  

        if position[0] <= 0 or position[0] >= x_s:
                x_vel = -x_vel      
                velx = -velx
                position[0] = round(position[0] + round((x_vel * number) / 20, 3), 1)
        if position[1] <= 0 or position[1] >= y_s:
                y_vel = -y_vel      
                vely = -vely
                position[1] = round(position[1] + round((y_vel * number) / 20, 3), 1)

        ball.rect.center = position
        goal_list = pygame.sprite.spritecollide(ball, HOLE, False)

        for hit in goal_list:
            goal = True
        if goal == True:
            ball.rect.center = (-50,0)
            screen.blit(bg_img, (0,0))
            BALL.update()
            BALL.draw(screen)
            PROPS.draw(screen)
            INACTIVE.draw(screen)
            pygame.display.flip()
            break
        
        if goal == True:
            break
        screen.blit(bg_img, (0,0))
        BALL.update()
        LevelLoad(level_num, screen, "action")
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