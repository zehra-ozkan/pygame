import pygame

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Object Example")

x = 200
y = 150

width = 50
height = 50

speed = 2
run = True
while run:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x -= speed
    if keys[pygame.K_RIGHT] and x< screen_width-width: 
        x += speed

    if keys[pygame.K_UP] and y>0: 
        y -= speed
    
    if keys[pygame.K_DOWN] and y< screen_height-height: 
        y += speed
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()