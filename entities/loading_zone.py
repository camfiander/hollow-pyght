import pygame
from pygame.locals import *
from sprite_controller import getPlayerGroup 

class LoadingZone(pygame.sprite.Sprite):
    def __init__(self, size) -> None:
        super().__init__()
        self.surf = pygame.Surface(size)
        self.surf.fill('green')
        self.rect = self.surf.get_rect()

    def trigger(self,player):
        pass


    def update(self):
        hits = pygame.sprite.spritecollide(self,getPlayerGroup(),False)
        if(hits):
            trigger(hits[0])

    
