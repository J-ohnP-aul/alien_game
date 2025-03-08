import pygame
from setting import Settings 
from ship import Ship
import gamefunc as gf

def run_game():
    # initialize the game and screen object
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien invasion")
    #ship institance
    ship = Ship(screen)
    
    # start the main loop of the game
    while True:
        #watch for keyboard and mouse events
        gf.checkEvents(ship)
        ship.update()
        gf.updateScreen(ai_setting, screen, ship)
       
run_game()