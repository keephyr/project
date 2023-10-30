import pygame

def Set_Pos(map, PROPS):
    import init_img as ii
    coordinates_box = []
    coordinates_water = []
    row_num = 0
    rect_amount = 0
    for row in map:
        place_num = 0
        for place in row:
            if place == 1:
                x = 80 * place_num
                y = 80 * row_num
                rect_amount += 1
                coordinates_box.append((x,y))
            elif place == 2:
                x = 80 * place_num
                y = 80 * row_num
                rect_amount += 1
                coordinates_water.append((x,y))
            place_num += 1
        row_num += 1
    num = 0
    try:
        for coordinate in coordinates_box:
            while True:
                ii.box_array[num].rect.center = (coordinate[0] + 40, coordinate[1] + 40)
                num = num + 1
                break
        num = 0
        for coordinate in coordinates_water:
            while True:
                ii.water_array[num].rect.center = (coordinate[0] + 40, coordinate[1] + 40)
                num = num + 1
                break
    except:
        pass

    PROPS.update()