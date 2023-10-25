def LevelLoad(level, screen, action, loading = False): 
    from init_img import BALL, LEVEL, PROPS, INACTIVE,HOLE, ball, x_s, y_s
    import init_img as i

    if loading == True and action != "next_level":
        ball.rect.center = ((x_s/2), (y_s - y_s / 6))
        LEVEL.update()
        BALL.update()
        print("updated")
        # print("level - ", level)
        for sprite in PROPS:
            sprite.rect.center = (-500,-500)
            PROPS.update()
        if level == 1:
            i.sand_prop.rect.center = (100,100)
            pass
        if level == 2:
            i.box.rect.center = (100,100)  
        if level == 3:
            i.box_2_col.rect.center = (100,200)     
        if level == 4:
            i.box_3_row.rect.center = (x_s // 2,200)    
        if level == 5:
            i.box_5_row.rect.center = (x_s // 2,200)   
        if level == 6:
            pass 
        if level == 11:
            i.sand_prop.rect.center = (100,100)
            i.ice_prop.rect.center = (x_s - 100, 100)
        loading = False
        PROPS.draw(screen)
    if action == "action":
        PROPS.draw(screen)
        HOLE.draw(screen)
        BALL.draw(screen)
        INACTIVE.draw(screen)
    PROPS.draw(screen)
    if type(level) == int:
        LEVEL.draw(screen)

    if action == "level" and loading == True:
        return True, level
    else:
        return loading, level
