import pygame
from pygame.locals import *
from config import HEIGHT,WIDTH

class Camera:
    def __init__(self,target,bounds : Rect=None):
        self.target = target
        self.pos = pygame.math.Vector2(0,0)
        self.rect = Rect(self.pos.x,self.pos.y,WIDTH,HEIGHT)
        self.bounds = bounds

    def update(self):
        #self.pos = self.target.pos
        if(not self.target is None):
            self.pos += (self.target.pos - self.pos)*0.15
        #assume this point is centered on the screen
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

        #bound the value if the camera would go outside bounds
        if(self.bounds):
            self.rect = self.rect.clamp(self.bounds)

CAM1 = Camera(None)
        
def follow(target):
    CAM1.target = target

def set_bounds(rect):
    CAM1.bounds = rect

def get_camera():
    return CAM1

def get_rect():
    return CAM1.rect

def update():
    CAM1.update()


