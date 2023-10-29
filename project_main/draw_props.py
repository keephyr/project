import pygame

def Set_Pos(map, PROPS):
    import init_img as ii
    coordinates = []
    row_num = 0
    rect_amount = 0
    print("hello")
    for row in map:
        place_num = 0
        for place in row:
            if place == 1:
                x = 80 * place_num
                y = 80 * row_num
                rect_amount += 1
                coordinates.append((x,y))
            place_num += 1
        row_num += 1
    num = 0
    try:
        for coordinate in coordinates:
            while True:
                ii.box_array[num].rect.center = (coordinate[0] + 40, coordinate[1] + 40)
                num = num + 1
                print(coordinate)
                print(ii.box_array[num].rect)
                break
    except:
        pass

    PROPS.update()