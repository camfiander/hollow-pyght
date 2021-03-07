import sys
import pygame
from pygame.locals import *
from config import HEIGHT, WIDTH, FPS
from player import *
from platform_builder import *
import camera
from sprite_controller import addCollision, addPlayer, addSprite, getAllSprites
import controls
from collision import Platform

 
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
roomSurface = pygame.Surface((WIDTH*4,HEIGHT*2))
uiSurface = pygame.Surface((WIDTH,HEIGHT))


pygame.display.set_caption("Game")

PT1 = Platform()
P1 = Player()
PB1 = PlatformBuilder()
addPlayer(P1)
addCollision(PT1)

addSprite(PT1,P1,PB1)

camera.follow(P1)

font = pygame.font.Font(None, 24)

#CAM1 = Camera(P1, roomSurface.get_rect())
#UI1 = UiController(uiSurface)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    controls.update()
    P1.move()
    P1.attack()
    getAllSprites().update()
    camera.update()


    displaysurface.fill('black')
    roomSurface.fill('black')
    if(PB1.plat):
        pygame.draw.rect(roomSurface,'blue',PB1.plat)
    for entity in getAllSprites():
        #TO CONSIDIER: this could be done with vectors
        #which might be more optimized
        roomSurface.blit(entity.surf, entity.rect)
    displaysurface.blit(roomSurface,(0,0),camera.get_rect())
    displaysurface.blit(font.render("grounded: {}".format(P1.grounded),True,(255,255,255)),(0,0))
    #displaysurface.blit(uiSurface,(0,0))
    pygame.display.update()
    FramePerSec.tick(FPS)