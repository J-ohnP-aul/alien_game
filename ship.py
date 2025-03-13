import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        '''initialize a ship and set its starting positions'''
        self.screen = screen
        self.ai_settings = ai_settings
        #load the ship img and get its rect
        self.image = pygame.image.load('image-40x90.jpg')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #start each neh shp at mid scren btm
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #decimaal val 4 ships center
        
        self.center = float(self.rect.centerx)
        
        #moving flag
        self.moving_r = False
        self.moving_l = False                                            
        
        
    def update(self):
        '''update ships posi based on the movment flag'''
        #update e ship center val !rect
        if self.moving_r and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_l and self.rect.left > 0:
           self.center -= self.ai_settings.ship_speed_factor
           
        # update rect obj
        self.rect.centerx = self.center
        
    def blitme(self):
        '''drw ship at initial loc'''
        self.screen.blit(self.image, self.rect)
        
        