from counter import Counter
from nail_interaction import NailInteractionType
from controls import get_inputs,get_pressed
from sprite_controller import getCollisionGroup
import pygame
from config import *
from pygame.locals import *
from nail import Nail
vec = pygame.math.Vector2  # 2 for two dimensional

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((40, 64))
        self.surf.fill('green')
        self.rect = self.surf.get_rect()
        self.nailInteractionType = NailInteractionType.NO_INTERACT
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.facing = vec(1,0)
        self.jumping = False
        self.grounded = False
        self.holding_jump = False
        self.knockbackVelocity = 0
        self.knockbackFrames = Counter(10)
        self.nail = Nail(self)
        self.invincibility = Counter(150)
        self.stun = Counter(30)
        self.nailCooldown = Counter(16)
        self.hp = 5
    
        self.counters = [
            self.invincibility,
            self.stun,
            self.knockbackFrames,
            self.nailCooldown       
           ]

    def move(self):
        self.acc = vec(0,GRAVITY)

        inputs = get_inputs()

        if inputs["left"] != inputs["right"]:
            self.vel.x = MOVE_SPEED if inputs["right"] else -MOVE_SPEED
            self.facing.x = 1 if inputs["right"] else -1
        else:
            self.vel.x = 0

        if(inputs["down"] and not self.grounded):
            self.facing.y = 1
        elif(inputs["up"]):
            self.facing.y = -1
        else:
            self.facing.y = 0

        if(get_pressed("jump") and self.grounded):
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
        self.pos += self.vel + 0.5 * self.acc + (self.knockbackVelocity if self.knockbackFrames else vec(0,0))

      #  if self.pos.x > WIDTH:
      #      self.pos.x = 0
      #  if self.pos.x < 0:
      #      self.pos.x = WIDTH

        #Collision goes here
        rectMoved = self.rect.copy()
        rectMoved.centerx = self.pos.x

        #platformRects = map(getRect, getCollisionGroup().sprites())
        platforms = getCollisionGroup().sprites()
        indices = rectMoved.collidelistall(platforms)
        if(indices):
            self.vel.x = 0
            if(rectMoved.left > self.rect.left):
                nextRight = platforms[indices[0]].rect.left - 1
                for x in indices:
                    nextRight = min(nextRight,platforms[x].rect.left - 1)
                rectMoved.right = nextRight
            elif(rectMoved.left < self.rect.left):
                nextLeft =  platforms[indices[0]].rect.right + 1
                for x in indices:
                    nextLeft = max(nextLeft,platforms[x].rect.right + 1)
                rectMoved.left = nextLeft
        rectMoved.bottom = self.pos.y
        indicesY = rectMoved.collidelistall(platforms)
        if(indicesY):
            
            self.vel.y = 0
            if(rectMoved.top >= self.rect.top):
                nextBottom = platforms[indicesY[0]].rect.top
                for x in indicesY:
                    nextBottom = min(nextBottom,platforms[x].rect.top)
                rectMoved.bottom = nextBottom
                self.grounded = True
            elif(rectMoved.top < self.rect.top):
                nextTop = platforms[indicesY[0]].rect.bottom
                for x in indicesY:
                    nextTop = max(nextTop,platforms[x].rect.bottom)
                rectMoved.top = nextTop
        else:
            self.grounded = rectMoved.move(0,1).collidelist(platforms) != -1


        self.pos.x = rectMoved.centerx
        self.pos.y = rectMoved.bottom        




        self.rect.midbottom = self.pos
        

    def jump(self):
        self.vel.y = JUMP_SPEED
        self.jumping = True
        self.holding_jump = True

    def attack(self):
        if(get_pressed("attack") and not self.nailCooldown):
            self.nail.swing()



    def update(self):
        #self.grounded = False
        #hits = pygame.sprite.spritecollide(self,getCollisionGroup(),False, )
        #if hits:
        #    self.grounded = True
        #    self.pos.y = hits[0].rect.top + 1
        #    self.vel.y = 0 
        #
        #self.rect.midbottom = self.pos
        for counter in self.counters:
            counter.update()

    def damage(self,dmg):
        if(dmg > 0 and not self.invincibility):
            self.hp -= dmg
            self.invincibility.reset()
            self.stun.reset()

    def knockback(self,direction,strength=4):
        self.knockbackFrames.reset()
        self.knockbackVelocity = direction * strength


   

    