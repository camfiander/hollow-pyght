from controls import get_inputs
from sprite_controller import getCollisionGroup
import pygame
from config import *
from pygame.locals import *
vec = pygame.math.Vector2  # 2 for two dimensional

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((40, 64))
        self.surf.fill('green')
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.jumping = False
        self.grounded = False
        self.holding_jump = False

    def move(self):
        self.acc = vec(0,GRAVITY)

        inputs = get_inputs()

        if inputs["left"] != inputs["right"]:
            self.vel.x = MOVE_SPEED if inputs["right"] else -MOVE_SPEED
        else:
            self.vel.x = 0

        if(inputs["jump"] and not self.holding_jump and self.grounded):
            self.jump()

        if(self.jumping and self.vel.y >= 0):
            self.jumping = False
        
        if(self.holding_jump and not inputs["jump"]):
            self.holding_jump = False
            if(self.jumping):
                self.jumping = False
                self.vel.y = 0
        
        self.vel += self.acc
        self.vel.y = min(self.vel.y,MAX_FALL_SPEED)
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
    
        self.rect.midbottom = self.pos
        

    def jump(self):
        self.vel.y = JUMP_SPEED
        self.jumping = True
        self.holding_jump = True

    def update(self):
        self.grounded = False
        hits = pygame.sprite.spritecollide(self,getCollisionGroup(),False)
        if hits:
            self.grounded = True
            self.pos.y = hits[0].rect.top + 1
            self.vel.y = 0

        self.rect.midbottom = self.pos

 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 
