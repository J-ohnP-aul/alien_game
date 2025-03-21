import pygame
from pygame.sprite import Group
from setting import Settings 
from ship import Ship
from alien import Alien
import gamefunc as gf

def run_game():
    # initialize the game and screen object
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode(
        (ai_setting.screen_width, ai_setting.screen_height))
    pygame.display.set_caption("Alien invasion")
    #alien instance
    alien = Alien(ai_setting, screen)
    #ship institance
    ship = Ship(ai_setting, screen)
    #group to store bullet en aln
    bullets = Group()
    aliens = Group()
    
    # a fleet of aliens 
    gf.create_fleet(ai_setting, screen, alien)
    
    # start the main loop of the game
    while True:
        #watch for keyboard and mouse events
        gf.checkEvents(ai_setting, screen, ship, bullets)
        ship.update()
        gf.updateBullets(bullets)
        gf.updateScreen(ai_setting, screen, ship, aliens, bullets)
       
run_game()