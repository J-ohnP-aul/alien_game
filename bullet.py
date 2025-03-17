import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''class managing bullet fird from ship'''
    def __init__(self, ai_setting, screen, ship):
        '''create abullt obj at ship crnt  pstn'''
        super(Bullet, self).__init__()
        self.screen = screen
        
        #crt bullet rect and set corect pstn
        self.rect = pygame.Rect(0, 0, ai_setting.bullet_width,
                                ai_setting.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        # store blt position decimal valuae
        self.y = float(self.rect.y)
        
        self.color = ai_setting.bullet_color
        self.speed_factor = ai_setting.bullet_speed_factor
        
    def update(self):
        ''''mv blt on the scrn'''
        pygame.draw.rect(self.screen, self.color, self.rect)
        #updt dcml psn of bult
        self.y -= self.speed_factor
        # updt rect pstn
        self.rect.y = self.y
    
    def drawBullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)