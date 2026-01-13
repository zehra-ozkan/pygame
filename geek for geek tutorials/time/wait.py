import pygame
from random import randint
from superobj import GameObj

def random_update(boost:GameObj, SCREEN_WIDTH:int, SCREEN_HEIGHT:int):
    random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
    boost_width = 25
    boost_height = 25
    boost_x = randint(int(SCREEN_WIDTH / 20), int(SCREEN_WIDTH - boost_width))
    boost_y = randint(int(SCREEN_WIDTH / 20), int(SCREEN_HEIGHT - boost_height))
    boost = GameObj(boost_width, boost_height, random_color, (boost_x, boost_y)) 
    return boost

def handle_gamer_movement(keys, player:GameObj, gamer_speed:int, SCREEN_WIDTH, SCREEN_HEIGHT):
    if keys[pygame.K_LEFT]:
        if player.position[0] > gamer_speed:
            player.transposeX(-1 * gamer_speed)
    if keys[pygame.K_RIGHT]:
        if player.position[0] + gamer_speed + player.width < SCREEN_WIDTH:
            player.transposeX(gamer_speed)
    if keys[pygame.K_UP]:
        if player.position[1] > gamer_speed:
            player.transposeY(-1 * gamer_speed)
    if keys[pygame.K_DOWN]:
        if player.position[1] + gamer_speed + player.height < SCREEN_HEIGHT:
            player.transposeY(gamer_speed)

def is_boost_activated(start, duration):
    if start == None:
        return False
    return pygame.time.get_ticks() - start < duration
def main():

    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    NORMAL_SPEED = 4
    RUN_SPEED = 12
    
    BOOST_DURATION = 3000 #this is 3 seconds
    
    GAMER_WIDTH = 50
    GAMER_HEIGHT = 50
    GAMER_COLOR = (255, 0, 0)
    GAMER_POS = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    gamer_speed = NORMAL_SPEED

    surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Wait Example')


    exit = False
    start = pygame.time.get_ticks()
    wait_time = 10500  # milliseconds in every 5 seconds
    boost = GameObj()
    player = GameObj(GAMER_WIDTH, GAMER_HEIGHT, GAMER_COLOR, GAMER_POS)
    surface.fill((0, 0, 0))
    
    boost_start = None
    boost_activated = False
    display_boost = True
    
    clock = pygame.time.Clock()  # create a Clock object
    while not exit:
        
        pygame.time.wait(50)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
                
        keys = pygame.key.get_pressed()  # returns a list of all keys
        handle_gamer_movement(keys,player, gamer_speed, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        if player.collide(boost):
            boost_start= pygame.time.get_ticks()
            boost_activated = True
            display_boost = False    
        
        boost_activated = is_boost_activated(boost_start , BOOST_DURATION)
        gamer_speed = RUN_SPEED if boost_activated else NORMAL_SPEED
        
        current = pygame.time.get_ticks()
        surface.fill((0, 0, 0))
        
        if current - start >= wait_time or boost.width == 10:
            start = current
            boost = random_update(boost, SCREEN_WIDTH, SCREEN_HEIGHT)
            display_boost = True
               
        
        if display_boost:
            boost.draw(surface)
        player.draw(surface)
        pygame.display.update()
        
        clock.tick(60)  # limit the loop to 60 FPS

        
        
                
if __name__ == "__main__":
    main()


