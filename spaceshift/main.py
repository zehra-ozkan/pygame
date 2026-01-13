import pygame

pygame.init()

WIDTH, HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))

exit = False

while not exit:
    for event in pygame.event.get(): #this gets all the events in the pygame
        if event.type == pygame.QUIT:
            exit = True

    #draw the game
    
    display_surface.fill('red')
    pygame.display.update()

#ensures that the game will close properly, safety net
pygame.quit()