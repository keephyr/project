def Change_btn_pos(biome):
    from init_img import BTNS, buttons, x_s, y_s, PLAIN, SAND
    for button in BTNS:
        if button.biome == "plain":
            if biome == 0:
                buttons[0].rect.center = ((x_s/2) - (x_s/10)),((y_s/10) * 3)
                buttons[1].rect.center = ((x_s/2)),((y_s/10) * 3)
                buttons[2].rect.center = ((x_s/2) + (x_s/10)),((y_s/10) * 3)

                buttons[3].rect.center = ((x_s/2)),((y_s/10) * 5)
                buttons[4].rect.center = ((x_s/2) - (x_s/10)),((y_s/10) * 5)
                buttons[5].rect.center = ((x_s/2) + (x_s/10)),((y_s/10) * 5)

                buttons[6].rect.center = ((x_s/2)),((y_s/10) * 7)
                buttons[7].rect.center = ((x_s/2) - (x_s/10)),((y_s/10) * 7)
                buttons[8].rect.center = ((x_s/2) + (x_s/10)),((y_s/10) * 7)
                
                buttons[9].rect.center = ((x_s/2)),((y_s/10) * 9)
            elif biome == 1:
                button.rect.center = (-500, 500)
        elif button.biome == "sand":
            if biome == 1:
                buttons[10].rect.center = ((x_s/2) - (x_s/10)),((y_s/10) * 3)
                # buttons[11].rect.center = ((x_s/2)),((y_s/10) * 3)
                # buttons[12].rect.center = ((x_s/2) + (x_s/10)),((y_s/10) * 3)

                # buttons[13].rect.center = ((x_s/2)),((y_s/10) * 5)
                # buttons[14].rect.center = ((x_s/2) - (x_s/10)),((y_s/10) * 5)
                # buttons[15].rect.center = ((x_s/2) + (x_s/10)),((y_s/10) * 5)

                # buttons[16].rect.center = ((x_s/2)),((y_s/10) * 7)
                # buttons[17].rect.center = ((x_s/2) - (x_s/10)),((y_s/10) * 7)
                # buttons[18].rect.center = ((x_s/2) + (x_s/10)),((y_s/10) * 7)
                
                # buttons[19].rect.center = ((x_s/2)),((y_s/10) * 9)
            elif biome == 0:
                button.rect.center = (-500, 500)
    PLAIN.update()
    SAND.update()
    BTNS.update()
    return BTNS, PLAIN, SAND

"""
((x_s/2)),((y_s/10) * 3)
((x_s/2) - (x_s/10)),((y_s/10) * 3)
((x_s/2) + (x_s/10)),((y_s/10) * 3)

((x_s/2)),((y_s/10) * 5)
((x_s/2) - (x_s/10)),((y_s/10) * 5)
((x_s/2) + (x_s/10)),((y_s/10) * 5)

((x_s/2)),((y_s/10) * 7)
((x_s/2) - (x_s/10)),((y_s/10) * 7)
((x_s/2) + (x_s/10)),((y_s/10) * 7)

((x_s/2)),((y_s/10) * 9)
"""