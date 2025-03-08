import pygame

class Ship():
    def __init__(self, screen):
        '''initialize a ship and set its starting positions'''
        self.screen = screen
        
        #load the ship img and get its rect
        self.image = pygame.image.load('image-40x120.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each neh shp at mid scren btm
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #moving flag
        self.moving_r = False
        
    def update(self):
        '''update ships posi based on the movment flag'''
        if self.moving_r:
            self.rect.centerx += 1
        
    def blitme(self):
        '''drw ship at initial loc'''
        self.screen.blit(self.image, self.rect)
        
        