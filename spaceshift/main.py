import pygame
from os.path import join

pygame.init()

WIDTH, HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("this is the caption")
exit = False

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


while not exit:
    for event in pygame.event.get(): #this gets all the events in the pygame
        if event.type == pygame.QUIT:
            exit = True
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        surface_x = surface_x + 1
    if keys[pygame.K_LEFT]:
        surface_x = surface_x - 1 
    #draw the game
    #surface_x = surface_x + 0.1
    display_surface.fill('darkgrey')#if you remove htis line it does not claer
    display_surface.blit(player_surf, (surface_x, 5))#putting one surface on another surface
    pygame.display.update()

#ensures that the game will close properly, safety net
pygame.quit()