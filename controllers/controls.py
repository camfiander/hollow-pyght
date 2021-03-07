import pygame
from pygame.locals import *

inputs = {
    "left":False,
    "right":False,
    "up":False,
    "down":False,
    "jump":False,
    "attack":False
}
lastInputs = {   
    "left":False,
    "right":False,
    "up":False,
    "down":False,
    "jump":False,
    "attack":False
}

def get_inputs():
    return inputs

def update():
    for key,val in inputs.items():
        lastInputs[key] = val

    pressed_keys = pygame.key.get_pressed()
    inputs["left"]= pressed_keys[K_LEFT]
    inputs["right"]= pressed_keys[K_RIGHT]
    inputs["up"]= pressed_keys[K_UP]
    inputs["down"]= pressed_keys[K_DOWN] 
    inputs[ "jump"]= pressed_keys[K_x]
    inputs["attack"]= pressed_keys[K_z]
    

def get_input(key):
    try:
        return inputs[key]
    except:
        return False

def get_pressed(key):
    return inputs[key] and not lastInputs[key]


