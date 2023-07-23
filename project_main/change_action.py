import pygame

def ChangeAction(action, btn_class, level = None):
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
    if level == None:
        return level, action
    elif level != None:
        return level_num, action
