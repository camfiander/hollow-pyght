import pygame
from pygame.locals import *
from sprite_controller import addCollision, addSprite, getCollisionGroup
from nail_interaction import NailInteractionType
from counter import Counter

class Nail(pygame.sprite.Sprite):
    offset = pygame.math.Vector2(100,100)
    def __init__(self,player):
        super().__init__()
        self.player = player
        self.pos = player.pos
        self.facing = player.facing
        self.surf = pygame.Surface((80,45))
        self.surf.fill('red')
        self.rect = self.surf.get_rect()
        self.lifeFrames = Counter(6)
        self.dmg = 1

    def update(self):
        self.rect.center = pygame.math.Vector2(0,-40) + self.pos + (Nail.offset.elementwise() * self.facing)
        if(not self.lifeFrames):
            super().kill()
        else:
            for hit in pygame.sprite.spritecollide(self,getCollisionGroup(),False):
                if(hit.nailInteractionType == NailInteractionType.DAMAGE or hit.nailInteractionType == NailInteractionType.DAMAGE_NO_KNOCKBACK or hit.nailInteractionType == NailInteractionType.BREAKABLE):
                    hit.damage(self.dmg)
                if(hit.nailInteractionType == NailInteractionType.KNOCKBACK or hit.nailInteractionType == NailInteractionType.DAMAGE):
                    hit.knockback(self.facing,4)
                    self.player.knockback(self.facing * -1)     
        self.lifeFrames.update()
        

    def swing(self):
        self.lifeFrames.reset()
        self.facing = pygame.math.Vector2(self.player.facing.x if self.player.facing.y == 0 else 0, self.player.facing.y)
        addSprite(self)

