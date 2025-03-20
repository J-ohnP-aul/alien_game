class Settings():
    '''all the seting at once'''
    def __init__(self):
        '''initialize the game setting'''
        #screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (111,191,255)
        #ship setting
        self.ship_speed_factor = 1
        #bullet setting
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 10
        self.bullet_color = 1, 1, 1 
        self.bullets_allowed = 4