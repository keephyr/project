import pygame
without_boxes = [1,3]
def LevelLoad(level, screen, action, loading = False): 
    from init_img import BALL, LEVEL, BOXES, INACTIVE,HOLE, ball, x_s, y_s
    global without_boxes
    # print(level)
    if loading == True and action != "next_level":
            ball.rect.center = ((x_s/2), (y_s/2))
            LEVEL.update()
            BALL.update()
            print("updated")
            loading = False
    if action == "action":
        HOLE.draw(screen)
        BALL.draw(screen)
        INACTIVE.draw(screen)
        if level in without_boxes:
            pass
        else:
            BOXES.draw(screen)
    elif level == 1:
        LEVEL.draw(screen)
    elif level == 2:
        LEVEL.draw(screen)
        BOXES.draw(screen)
    elif level == 3:
        LEVEL.draw(screen)
    if action == "level" and loading == True:
        return True, level
    else:
        return loading, level
