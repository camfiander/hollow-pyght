import pygame
from pygame.locals import *

class UiController:
    def __init__(self,surf):
        self.surf = surf
        self.elementList = []
        if(not pygame.font.get_init()):
            pygame.font.init()
        print(pygame.font.get_fonts())
        
    