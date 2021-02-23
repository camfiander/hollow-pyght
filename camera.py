import pygame
from pygame.locals import *
from config import HEIGHT,WIDTH

class Camera:
    def __init__(self,target,bounds : Rect):
        self.target = target
        self.pos = target.pos
        self.rect = Rect(self.pos.x,self.pos.y,WIDTH,HEIGHT)
        self.bounds = bounds

    def update(self):
        self.pos = self.target.pos

        #assume this point is centered on the screen
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

        #bound the value if the camera would go outside bounds
        self.rect = self.rect.clamp(self.bounds)
