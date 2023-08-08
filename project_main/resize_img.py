import pygame
# from init_img import *

pygame.init()

def resize(scale, Widgets, x_s, y_s):
    import init_img as i

    # print(type(i.start_btn))
    # print(type(i.START))
    # print(vars(i))
    # for obj in vars(i):
    #     print(obj)
    #     if type(obj) == "init_img.Widget":
    #         # obj.Resize(scale)
    #         print(obj)

    i.start_btn.Resize(scale)
    i.set_btn.Resize(scale)
    i.exit_btn.Resize(scale)
    i.Name.Resize(scale)

    i.START.update() # START

    i.back_btn.Resize(scale)

    i.N1_btn.Resize(scale)
    i.N2_btn.Resize(scale)
    i.N3_btn.Resize(scale)

    i.Level_select_Name.Resize(scale)

    i.LVL_S.update() # LEVEL SELECT

    i.pause_btn.Resize(scale)
    i.pause.Resize(scale)
    i.resume_btn.Resize(scale)

    i.PAUSE.update()

    i.res.Resize(scale)

    i.SETTINGS.update()

    i.ball.Resize(scale)

    i.apply.Resize(scale)

    slider = Widgets[0]
    textBox = Widgets[1]

    slider_height, slider_width = int(50 * scale), int(400 * scale)

    slider.setHeight(slider_height)
    slider.setWidth(slider_width)
    slider.setX(int(x_s/2.3))
    slider.setY(int(((y_s/10) * 2.7)))

    textBox_height, textBox_width = int(50 * scale), int(200 * scale)

    textBox.setHeight(textBox_height)
    textBox.setWidth(textBox_width)
    textBox.setX(int(x_s/1.3))
    textBox.setY(int(((y_s/10) * 2.7)))

    return slider, textBox
