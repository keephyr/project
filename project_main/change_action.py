import pygame

def ChangeAction(action, btn_class, level = None, resize = False):
    if action == "Start":

        if btn_class == "start":
            action = "lvl_select"
        elif btn_class == "set":
            action = "settings"
        elif btn_class == "exit":
            action = "exit"
        else:
            action = "Start"

    elif action == "lvl_select":

        if btn_class == "back":
            action = "Start"
        elif level != None:
            action = "level"
            level_num = level

    elif action == "settings":

        if btn_class == "back":
            action = "Start"
        elif btn_class == "apply":
            action = "settings"
            resize = True

    elif action == "level":
        if btn_class == "pause":
            action = "pause"

    elif action == "pause":

        if btn_class == "res":
            action = "level"
        elif btn_class == "set":
            action = "settings"
        elif btn_class == "exit":
            action = "Start"
    if level == None:
         return level, action, resize
    elif level != None:
         return level_num, action, resize