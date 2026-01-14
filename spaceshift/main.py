import pygame
from os.path import join
from random import randrange

class Player(pygame.sprite.Sprite): #inheriting from sprite sprite is a class with a reectangle and a surface in pygame
    def __init__(self, groups):
        super().__init__(groups)
        self.image = pygame.image.load(join('spaceshift','images', 'player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(WIDTH / 2, HEIGHT / 2))
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 240
        
    def update(self, dt):
        print("ship is being updated")

        keys =  pygame.key.get_pressed()
        
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])#htis successfully replaces the above code
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction.magnitude() > 0 else self.direction #this stabilises teh speed
        self.rect.center = self.rect.center +  self.direction * self.speed * dt #multipllying with dt makes the movement speed independent from fps

        

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

all_sprites = pygame.sprite.Group()
player = Player(all_sprites)


star_surface = pygame.image.load(join('spaceshift','images', 'star.png')).convert_alpha()
star_coordinates = []
for i in range (20):
    star_coordinates.append((randrange(0, WIDTH), randrange(0, HEIGHT)))

meteor_surface = pygame.image.load(join('spaceshift', 'images', 'meteor.png')).convert_alpha()
meteor_rectangle = meteor_surface.get_frect(center=(WIDTH / 2, HEIGHT/2))

laser_surface = pygame.image.load(join('spaceshift', 'images', 'laser.png')).convert_alpha()
laser_rectangle = laser_surface.get_frect(bottomleft=(20, HEIGHT - 20))





while not exit:
    delta_time = clock.tick(120) / 1000 #delta time measrures hte time took by the computer to render in between the last 2 frames, how much time has changed since the last 2 frames, different in everty computer
    for event in pygame.event.get(): #this gets all the events in the pygame
        if event.type == pygame.QUIT:
            exit = True
         
    all_sprites.update(delta_time)
    keys = pygame.key.get_pressed()
    
        
    #laser
    k = pygame.key.get_just_pressed()
    if k[pygame.K_SPACE]:
        print("space pressed")
  
    
        
    display_surface.fill('darkgrey')#if you remove htis line it does not claer
    for i in star_coordinates:
        display_surface.blit(star_surface, i)#putting one surface on another surface
    
    
    #display_surface.blit(player_surf, (surface_x, 5))#putting one surface on another surface
    
      
    display_surface.blit(meteor_surface, meteor_rectangle)    
    display_surface.blit(laser_surface, laser_rectangle)    
    display_surface.blit(player.image, player.rect)
    all_sprites.draw(display_surface)
    pygame.display.update()

#ensures that the game will close properly, safety net
pygame.quit()