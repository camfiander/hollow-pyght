import sys
import pygame
from pygame.locals import *
from config import HEIGHT, WIDTH, FPS
from player import *
from platform_builder import *
from camera import *
from sprite_controller import addCollision, addSprite, getAllSprites
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
roomSurface = pygame.Surface((WIDTH*4,HEIGHT*2))
uiSurface = pygame.Surface((WIDTH,HEIGHT))


pygame.display.set_caption("Game")




PT1 = platform()
P1 = Player()
PB1 = PlatformBuilder()

addCollision(PT1)



addSprite(PT1,P1,PB1)

CAM1 = Camera(P1, roomSurface.get_rect())
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.move()
    getAllSprites().update()
    CAM1.update()

    
    displaysurface.fill('black')
    roomSurface.fill('black')
    if(PB1.plat):
        pygame.draw.rect(displaysurface,'blue',PB1.plat)
    for entity in getAllSprites():
        #TO CONSIDIER: this could be done with vectors
        #which might be more optimized
        roomSurface.blit(entity.surf, entity.rect)
    displaysurface.blit(roomSurface,(0,0),CAM1)
    pygame.display.update()
    FramePerSec.tick(FPS)