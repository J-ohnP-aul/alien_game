import sys
import pygame

def checkEvents():
    '''respons 2 user events'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
def updateScreen(ai_settings, screen, ship):
    '''updt img on scrn and flip to the new screen'''
    #redraw the screen drng each loop pass
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    #make the most recent drn action on the screen
    pygame.display.flip()
    