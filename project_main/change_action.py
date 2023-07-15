import pygame

def ChangeAction(action,btn_class):
    if action == "Start":
        if btn_class == "start":
            action = "lvl_select"
        elif btn_class == "exit":
            action = "exit"
        else:
            action = "Start"
    elif action == "lvl_select":
        if btn_class == "back":
            action = "Start"


    return action