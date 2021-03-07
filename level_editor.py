import json
import sys
import pygame
from pygame.locals import *
from config import HEIGHT, WIDTH, FPS
from player import *
from platform_builder import *
from camera import *
from controls import get_inputs

pygame.init()
vec = pygame.math.Vector2
FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Level Editor")

all_sprites = pygame.sprite.Group()

PB1 = PlatformBuilder()

class LevelEditorController:
    def __init__(self):
        self.pos = vec(0,0)

    def update():
        pass

def export(room):
    roomDict = {
        "meta": {
            "roomId": 1,
            "height": 900,
            "width": 2000
        },

        "platforms": [
            {
                "top":x.rect.top,
                "left":x.rect.left,
                "height":x.rect.height,
                "width":x.rect.width
            } for x in room.platforms],
        
        "player":{
            "x":100,
            "y":100
        }
    }

    with open('room.json','w') as outfile:
        json.dump(roomDict,outfile)



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    


    displaysurface.fill('black')
    
    if(PB1.plat):
        pygame.draw.rect(displaysurface,'blue',PB1.plat)
    for entity in all_sprites:
        #TO CONSIDIER: this could be done with vectors
        #which might be more optimized
        roomSurface.blit(entity.surf, entity.rect)
    displaysurface.blit(roomSurface,(0,0),CAM1.rect)
    displaysurface.blit(uiSurface,(0,0))
    pygame.display.update()
    FramePerSec.tick(FPS)