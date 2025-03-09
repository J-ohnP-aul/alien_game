import sys
import pygame

def checkEvents(ship):
    '''respons 2 user events'''
    def checkKeyDown(event, ship):
        '''respond to key presses'''
        if event.key == pygame.K_RIGHT:
            ship.moving_r = True
        elif event.key == pygame.K_LEFT:
            ship.moving_l = True
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
            checkKeyDown(event, ship)
        elif event.type == pygame.KEYUP:
            checkKeyup(event, ship)                
            
def updateScreen(ai_settings, screen, ship):
    '''updt img on scrn and flip to the new screen'''
    #redraw the screen drng each loop pass
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #make the most recent drn action on the screen
    pygame.display.flip()
    
