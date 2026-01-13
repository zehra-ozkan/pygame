import pygame
from os.path import join
from random import randrange


pygame.init()

WIDTH, HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("this is the caption")
exit = False

clock = pygame.time.Clock()

#surface

surf = pygame.Surface((100, 200))
surf.fill('purple')
surface_x = 100

#importing an image
#images should be converted so that the game runs faster
# image has transparent pixels -> pixels::convert_alpha()
# image has no transparent pixels -> pixels:convert()
path = join('spaceshift','images', 'player.png')
print(path)
player_surf  = pygame.image.load(path).convert_alpha()
#player_surf  = pygame.image.load('./spaceshift/images/player.png')# this might not have worked in macos where it expects \
#player_rect = player_surf.get_frect(center=(0,0))
player_rect = player_surf.get_frect(center=(WIDTH / 2, HEIGHT / 2))

star_surface = pygame.image.load(join('spaceshift','images', 'star.png')).convert_alpha()
star_coordinates = []
for i in range (20):
    star_coordinates.append((randrange(0, WIDTH), randrange(0, HEIGHT)))

meteor_surface = pygame.image.load(join('spaceshift', 'images', 'meteor.png')).convert_alpha()
meteor_rectangle = meteor_surface.get_frect(center=(WIDTH / 2, HEIGHT/2))

laser_surface = pygame.image.load(join('spaceshift', 'images', 'laser.png')).convert_alpha()
laser_rectangle = laser_surface.get_frect(bottomleft=(20, HEIGHT - 20))



dir = pygame.math.Vector2(2, -2)
speed = 60

while not exit:
    dt = clock.tick(60) / 1000 #delta time measrures hte time took by the computer to render in between the last 2 frames, how much time has changed since the last 2 frames, different in everty computer
    print("dt",dt)
    for event in pygame.event.get(): #this gets all the events in the pygame
        if event.type == pygame.QUIT:
            exit = True
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        player_rect.right = player_rect.right + 1 if player_rect.right < WIDTH else player_rect.right
    if keys[pygame.K_LEFT]:
        player_rect.right = player_rect.right - 1 if player_rect.left > 0 else player_rect.right
    #draw the game
    #surface_x = surface_x + 0.1
    #order of the drawing matters!! background first otherwise nothing will be seen
    
    for i in star_coordinates:
        display_surface.blit(star_surface, i)#putting one surface on another surface
    
    
    #display_surface.blit(player_surf, (surface_x, 5))#putting one surface on another surface
    
    #bounce from left to right
    if player_rect.right >= WIDTH or player_rect.left <=0:
        dir.x = dir.x * -1
        
    if player_rect.bottom >= HEIGHT or player_rect.top <=0:
        dir.y = dir.y * -1
        
    #print(dir)
    
    #print(player_rect.center)
    player_rect.center = player_rect.center + dir * speed * dt
    #print(player_rect.center)
    
    display_surface.fill('darkgrey')#if you remove htis line it does not claer
    display_surface.blit(meteor_surface, meteor_rectangle)    
    display_surface.blit(laser_surface, laser_rectangle)    
    display_surface.blit(player_surf, player_rect)#putting one surface on another surface
    
    pygame.display.update()

#ensures that the game will close properly, safety net
pygame.quit()