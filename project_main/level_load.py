import pygame
without_boxes = [1]
def LevelLoad(level, screen, action, loading = False): 
    from init_img import BALL, LEVEL, BOXES, INACTIVE,HOLE, ball, x_s, y_s, box, box_2_col, box_3_row, box_5_row
    global without_boxes
    if loading == True and action != "next_level":
        ball.rect.center = ((x_s/2), (y_s - y_s / 6))
        LEVEL.update()
        BALL.update()
        print("updated")
        print("level - ", level)
        if level == 1:
            print("level1")
            box.rect.center = (-500,-500)
            box_2_col.rect.center = (-500,-500)
            box_3_row.rect.center = (-500,-500)
            box_5_row.rect.center = (-500,-500)
        if level == 2:
            print("level2")
            box.rect.center = (100,100)
            box_2_col.rect.center = (-500,-500)
            box_3_row.rect.center = (-500,-500)
            box_5_row.rect.center = (-500,-500)    
        if level == 3:
            print("level3")
            box.rect.center = (-500,-500)
            box_2_col.rect.center = (100,200)
            box_3_row.rect.center = (-500,-500)
            box_5_row.rect.center = (-500,-500)      
        if level == 4:
            print("level4")
            box.rect.center = (-500,-500)
            box_2_col.rect.center = (-500,-500)
            box_3_row.rect.center = (x_s //2,200)
            box_5_row.rect.center = (-500,-500)       
        if level == 5:
            print("level5")
            box.rect.center = (-500,-500)
            box_2_col.rect.center = (-500,-500)
            box_3_row.rect.center = (-500,-500)
            box_5_row.rect.center = (-500,-500)   
        if level == 6:
            print("level6")
            box.rect.center = (-500,-500)
            box_2_col.rect.center = (-500,-500)
            box_3_row.rect.center = (-500,-500)
            box_5_row.rect.center = (-500,-500)           
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
        BOXES.draw(screen)
        LEVEL.draw(screen)
    elif level == 3:
        BOXES.draw(screen)
        LEVEL.draw(screen)
    elif level == 4:
        BOXES.draw(screen)
        LEVEL.draw(screen)
    elif level == 5:
        BOXES.draw(screen)
        LEVEL.draw(screen)
    elif level == 6:
        BOXES.draw(screen)
        LEVEL.draw(screen)
    if action == "level" and loading == True:
        return True, level
    else:
        return loading, level
