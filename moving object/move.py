import pygame
from random import randrange
pygame.init()

def _handle_move(x : int , y : int, speed:int, keys, screen_width, screen_height, width, height):
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x< screen_width-width: 
        x = x +  speed

    if keys[pygame.K_UP] and y > 0: 
        y -= speed
    if keys[pygame.K_DOWN] and y < screen_height-height: 
        y += speed
    return x, y

def _handle_collision(x, y , boost_x, boost_y,boost_width, boost_height):
    if x in range(boost_x, boost_x + boost_width) and y in range(boost_y, boost_y + boost_height):
        return True
    return False
    

screen_width = 800
screen_height = 600

boost_x = randrange(screen_width)
boost_y = randrange(screen_height)
boost_width = 10
boost_height = 10

x = 200
y = 150
width = 50
height = 50

WALK_SPEED = 2
RUN_SPEED = 5
speed = WALK_SPEED

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Object Example")
run = True
while run:
    
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        
    keys = pygame.key.get_pressed()
    x, y = _handle_move(x , y, speed, keys, screen_width, screen_height, width, height)
    collision = False
    collision = _handle_collision(x, y , boost_x, boost_y, boost_width, boost_height)
    print(collision)
    speed = speed + RUN_SPEED if collision else speed
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    
    if not collision:
        pygame.draw.rect(screen, (50, 100, 200), (boost_x, boost_y, boost_width, boost_height))
    pygame.display.update()
pygame.quit()

