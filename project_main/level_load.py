from draw_props import Set_Pos
import json
from os import path

file_path = path.join(path.dirname(__file__), '')
text = open(file_path + "maps_plain.json", "r")
data = json.load(text)

def LevelLoad(level, screen, action, hit, loading = False): 
    from init_img import BALL, LEVEL, PROPS, INACTIVE,HOLE, ball, x_s, y_s, text_surface, my_font
    import init_img as i

    if loading == True and action != "next_level" and action != "restart":
        ball.rect.center = ((x_s/2), (y_s - y_s / 6))
        LEVEL.update()
        BALL.update()
        print("updated")
        # print("level - ", level)
        for sprite in PROPS:
            sprite.rect.center = (-500,-500)
            PROPS.update()
            hit = 0

        for map in data["levels"]:
            if level == 1:
                pass
            else:
                map_num = "map" + str(level)
                Set_Pos(map[str(map_num)], PROPS)
        # if level == 1:
        #     pass
        # if level == 2:
        #     Set_Pos(i.map2, PROPS)
        # if level == 3:
        #     Set_Pos(i.map3, PROPS)  
        # if level == 4:
        #     Set_Pos(i.map4, PROPS)  
        # if level == 5:
        #     Set_Pos(i.map5, PROPS)
        # if level == 6:
        #     Set_Pos(i.map6, PROPS)
        # if level == 7:
        #     Set_Pos(i.map7, PROPS)
        # if level == 8:
        #     Set_Pos(i.map8, PROPS)
        # if level == 9:
        #     Set_Pos(i.map9, PROPS)
        # if level == 10:
        #     Set_Pos(i.map10, PROPS)
        # if level == 11:
        #     i.sand_prop.rect.center = (100,100)
        #     i.ice_prop.rect.center = (x_s - 100, 100)
        loading = False
        PROPS.draw(screen)
    if action == "action":
        PROPS.draw(screen)
        HOLE.draw(screen)
        BALL.draw(screen)
        INACTIVE.draw(screen)
        text_surface = my_font.render(f"Your score: {hit}", False, (0, 0, 0))
        screen.blit(text_surface, (200, 300))
    PROPS.draw(screen)
    if type(level) == int:
        LEVEL.draw(screen)
    if action == "level" and loading == True:
        return True, level, hit
    else:
        return loading, level, hit
