import sys
import pygame
from bullet import Bullet

def checkEvents(ai_setting, screen, ship, bullets):
    '''respons 2 user events'''
    def checkKeyDown(event, ai_setting, screen, ship, bullets):
        '''respond to key presses'''
        if event.key == pygame.K_RIGHT:
            ship.moving_r = True
        elif event.key == pygame.K_LEFT:
            ship.moving_l = True
        elif event.key == pygame.K_SPACE:
            fireBullets(ai_setting, screen, ship, bullets)
        elif event.key == pygame.K_q:
            sys.exit()
    def checkKeyup(event, ship):
        '''respond to key releases'''
        if event.key == pygame.K_RIGHT:
            ship.moving_r = False
        elif event.key == pygame.K_LEFT:
            ship.moving_l = False
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            checkKeyDown(event, ai_setting, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            checkKeyup(event, ship)                
            
def updateScreen(ai_setting, screen, ship, alien, bullets):
    '''updt img on scrn and flip to the new screen'''
    screen.fill(ai_setting.bg_color)
    #redrw blt behind ship & alien
    for bullet in bullets.sprites():
        bullet.drawBullet()
    #redraw the screen drng each loop pass
    ship.blitme()
    alien.blitme()
    
    #make the most recent drn action on the screen
    pygame.display.flip()
    
def updateBullets(bullets):
    '''updt blt psn en get rid of old'''
    bullets.update()        
    # dl old blt
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
        # print(len(bullets))
def fireBullets(ai_setting, screen, ship, bullets):
    '''fire blt if lim !reached'''
    #crt a nw blt and addd it to the grp
    if len(bullets) < ai_setting.bullets_allowed:
        new_bullet = Bullet(ai_setting, screen, ship)
        bullets.add(new_bullet)