import sys
import pygame
from config import HEIGHT, WIDTH, FPS
from pygame.locals import *
from player import *
from platform_builder import *
from sprite_controller import addCollision, addSprite, getAllSprites
 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional

FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")




PT1 = platform()
P1 = Player()
PB1 = PlatformBuilder()

addCollision(PT1)



addSprite(PT1,P1,PB1)

 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.move()
    getAllSprites().update()
    displaysurface.fill('black')
    if(PB1.plat):
        pygame.draw.rect(displaysurface,'blue',PB1.plat)
    for entity in getAllSprites():
        displaysurface.blit(entity.surf, entity.rect)
 
    pygame.display.update()
    FramePerSec.tick(FPS)