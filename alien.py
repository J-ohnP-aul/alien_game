import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''initialize aln st ps'''
    
    def __init__(self, ai_setting, screen):
        super(Alien, self).__init__()
        self.screen = screen        
        self.ai_setting = ai_setting
        #load aln img en sert its rect atrr
        self.image = pygame.image.load("image-40x120.jpg")
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        self.x = float(self.rect.x)
        
    def blitme(self):
        '''alin drw'''
        self.screen.blit(self.image, self.rect)
        
