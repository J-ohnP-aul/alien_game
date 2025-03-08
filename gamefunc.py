import sys
import pygame

def checkEvents(ship):
    '''respons 2 user events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_r = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_r = False
                
            
def updateScreen(ai_settings, screen, ship):
    '''updt img on scrn and flip to the new screen'''
    #redraw the screen drng each loop pass
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #make the most recent drn action on the screen
    pygame.display.flip()
    
