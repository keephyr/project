import pygame
# from init_img import *

pygame.init()

def resize(scale):
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