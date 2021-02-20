import pygame
from pygame.locals import *

all_sprites = pygame.sprite.Group()
collision_group = pygame.sprite.Group()

def addSprite(*args):
    for spr in args:
        all_sprites.add(spr)

def addCollision(*args):
    for spr in args:
        collision_group.add(spr)

def getAllSprites():
    return all_sprites

def getCollisionGroup():
    return collision_group