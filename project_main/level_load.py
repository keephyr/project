import pygame
biom = 0
def LevelLoad(level, screen, action, loading = False): 
    from init_img import BALL, LEVEL, BOXES, INACTIVE,HOLE, ball, x_s, y_s, box, box_2_col, box_3_row, box_5_row
    if loading == True and action != "next_level":
        ball.rect.center = ((x_s/2), (y_s - y_s / 6))
        LEVEL.update()
        BALL.update()
        print("updated")
        print("level - ", level)
        for sprite in BOXES:
            sprite.rect.center = (-500,-500)
        if level == 1:
            print("level1")
            pass
        if level == 2:
            print("level2")
            box.rect.center = (100,100)  
        if level == 3:
            print("level3")
            box_2_col.rect.center = (100,200)     
        if level == 4:
            print("level4")
            box_3_row.rect.center = (x_s //2,200)    
        if level == 5:
            print("level5")
            box_5_row.rect.center = (x_s //2,200)   
        if level == 6:
            print("level6")
            pass         
        loading = False
        BOXES.draw(screen)
    if action == "action":
        HOLE.draw(screen)
        BALL.draw(screen)
        INACTIVE.draw(screen)
        BOXES.draw(screen)
    elif level == 1:
        LEVEL.draw(screen)
    elif level == 2:
        LEVEL.draw(screen)
    elif level == 3:
        LEVEL.draw(screen)
    elif level == 4:
        LEVEL.draw(screen)
    elif level == 5:
        LEVEL.draw(screen)
    elif level == 6:
        LEVEL.draw(screen)
    BOXES.draw(screen)
    if action == "level" and loading == True:
        return True, level
    else:
        return loading, level
