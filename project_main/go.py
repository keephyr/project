import pygame
from get_size import GetScreenSize

clock = pygame.time.Clock()
clicked = False
pos1 = None
pos2 = None

def go(velx, vely, position, ball):
    from level_load import LevelLoad
    from draw import screen, main_screen, level_num, screen
    from init_img import bg_img, BALL, HOLE, INACTIVE, PROPS, WATER
    x_s, y_s = GetScreenSize()
    x_vel = 1
    y_vel = 1
    number = .9
    goal = False
    lost = False
    ball_position = 0
    while x_vel != 0 and y_vel != 0:
        x_vel = round(velx * number, 2)
        y_vel = round(vely * number, 2)

        hit_list = pygame.sprite.spritecollide(ball, PROPS, False)
        if len(hit_list) != 0:
            for box in hit_list:
                if box.prop_class == "box":
                    if ball.rect.right >= box.rect.left and ball.rect.left < box.rect.left: #left side of the box
                        if ball.rect.top >= box.rect.top or ball.rect.bottom <= box.rect.bottom:
                                x_vel = -abs(x_vel)
                                velx = -abs(velx)
                                position[0] = round(position[0] + round((x_vel * number) / 20, 3), 1)
                    elif ball.rect.left <= box.rect.right and ball.rect.right > box.rect.right: # right side of the box
                        if ball.rect.top >= box.rect.top or ball.rect.bottom <= box.rect.bottom:
                                x_vel = abs(x_vel)
                                velx = abs(velx)
                                position[0] = round(position[0] + round((x_vel * number) / 20, 3), 1)
                    elif ball.rect.top <= box.rect.bottom and ball.rect.bottom > box.rect.bottom: # bottom side of the box
                        if ball.rect.left >= box.rect.left or ball.rect.right <= box.rect.right:
                                y_vel = abs(y_vel)
                                vely = abs(vely)
                                position[1] = round(position[1] + round((y_vel * number) / 20, 3), 1)
                    elif ball.rect.bottom >= box.rect.top and ball.rect.top < box.rect.top: # bottom side of the box
                        if ball.rect.left >= box.rect.left or ball.rect.right <= box.rect.right:
                                y_vel = -abs(y_vel)
                                vely = -abs(vely)
                                position[1] = round(position[1] + round((y_vel * number) / 20, 3), 1)
                elif box.prop_class != "box":
                    position[0] = round(position[0] + round((x_vel * number) / 20, 3), 1)
                    position[1] = round(position[1] + round((y_vel * number) / 20, 3), 1)
                    if box.prop_class == "sand":
                        number = number - 0.05
                        if number < 0:
                            number = 0
                        number = round(number,2)
                    elif box.prop_class == "ice":
                        number = number - 0.01
                        if number < 0:
                            number = 0
                        number = round(number,2)
                    elif box.prop_class == "water":
                        number = 0
                        x_vel = 0
                        y_vel = 0
                    if box.prop_class != "sand" and box.prop_class != "ice":
                        number = number - 0.03
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

        lost_list = pygame.sprite.spritecollide(ball, WATER, False)

        for loss in lost_list:
            lost = True
        for hit in goal_list:
            goal = True
        if goal == True or lost == True:
            ball_position = ball.rect.center

            ball.rect.center = (-50,-50)
            screen.blit(bg_img, (0,0))
            BALL.update()
            BALL.draw(screen)
            PROPS.draw(screen)
            INACTIVE.draw(screen)
            pygame.display.flip()
            break
        screen.blit(bg_img, (0,0))
        BALL.update()
        LevelLoad(level_num, screen, "action")
        main_screen.blit(pygame.transform.scale(screen, main_screen.get_rect().size), (0, 0))
        pygame.display.flip()

    return goal, lost, ball_position

def clicked_func(ball):
    global clicked, pos1, pos2
    if pygame.mouse.get_pressed()[0] == True and clicked == False:
        clicked = True
        pos1 = pygame.mouse.get_pos()
        return False, False, 0
    elif pygame.mouse.get_pressed()[0] == False and clicked == True:
        clicked = False
        pos2 = pygame.mouse.get_pos()
        goal, lost, ball_position = vel(pos1, pos2, ball)
        return goal, lost, ball_position
    else:
        return False, False, 0

def vel(pos1, pos2, ball):
    velx = pos1[0] - pos2[0]
    vely = pos1[1] - pos2[1]
    position = list(ball.rect.center)
    goal, lost, ball_position = go(velx, vely, position,ball)
    return goal, lost, ball_position