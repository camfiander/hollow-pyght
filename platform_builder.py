import pygame
from pygame.locals import *
from sprite_controller import addCollision, addSprite
import camera
from nail_interaction import NailInteractionType

class PlatformBuilder(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill('red')
        self.rect = self.surf.get_rect()
        self.drawing = False
        self.plat = None
        self.anchor = (0,0)
        self.nailInteractionType = NailInteractionType.NO_INTERACT

    def update(self):
        if(pygame.mouse.get_focused()):
            mouse_pos = pygame.mouse.get_pos()
            self.rect.left = mouse_pos[0] + camera.get_rect().left
            self.rect.top = mouse_pos[1] + camera.get_rect().top 
            if(pygame.mouse.get_pressed(num_buttons=3)[0]):
                if(not self.drawing):
                    self.drawing = True
                    self.anchor = self.rect.topleft
                    self.plat = pygame.Rect(self.rect.left, self.rect.top,1,1)
                if(self.rect.left < self.anchor[0]):
                    self.plat.width = self.anchor[0] - self.rect.left
                    self.plat.left = self.rect.left
                else:
                    self.plat.width = self.rect.left - self.plat.left
                if(self.rect.top < self.anchor[1]):
                    self.plat.height = self.anchor[1] - self.rect.top
                    self.plat.top = self.rect.top
                else:
                    self.plat.height = self.rect.top - self.plat.top
            elif(self.drawing and not self.plat is None):
                self.drawing = False
                platformObject = PlatformBuilderPlatform(self.plat)
                addSprite(platformObject)
                addCollision(platformObject)
                self.plat = None

                
class PlatformBuilderPlatform(pygame.sprite.Sprite):
    def __init__(self, rect) -> None:
        super().__init__()
        self.invincibility = -1
        self.surf = pygame.Surface(rect.size)
        self.surf.fill('blue')
        self.rect = self.surf.get_rect()
        self.rect.topleft = rect.topleft
        self.nailInteractionType = NailInteractionType.NO_INTERACT


                

                    