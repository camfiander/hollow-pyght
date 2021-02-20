import pygame
from pygame.locals import *

def get_inputs():
    pressed_keys = pygame.key.get_pressed()
    return {
        "left": pressed_keys[K_LEFT],
        "right": pressed_keys[K_RIGHT],
        "up": pressed_keys[K_UP],
        "down": pressed_keys[K_DOWN],
        "jump": pressed_keys[K_SPACE],
    }