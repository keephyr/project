import pygame
level_num = 0
def ChangeAction(action, btn_class, level = None, resize = False):
    global level_num
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
        elif btn_class[0] == "N":
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
            print(level_num)
            print(level)
            level_num = level

    elif action == "pause":

        if btn_class == "res":
            action = "level"
        elif btn_class == "set":
            action = "settings"
        elif btn_class == "exit":
            action = "Start"

    elif action == "next_level":
        if btn_class == "pause":
            action = "pause"
        elif btn_class == "next":
            level += 1
            action = "level" 
        
    return level_num, action, resize