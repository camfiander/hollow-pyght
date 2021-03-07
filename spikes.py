import pygame
from pygame.locals import *
from nail_interaction import NailInteractionType
from sprite_controller import getPlayerGroup
class Spikes(pygame.sprite.Sprite):
    def __init__(self, size) -> None:
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill('blue')
        self.rect = self.surf.get_rect()
        self.nailInteractionType = NailInteractionType.KNOCKBACK
    def update(self):
        hits = pygame.sprite.spritecollide(self,getPlayerGroup(),False)
        for hit in hits:
            try:
                hit.damage(1)
            except:
                pass
            
