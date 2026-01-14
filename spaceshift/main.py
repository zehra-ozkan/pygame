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
        
        #cooldown
        self.can_shoot = True
        self.laser_shoot_time = 0
        self.cooldown_duration = 200
    
    def laser_timer(self):
        if self.can_shoot:
            return
        current_time = pygame.time.get_ticks()
        if current_time - self.laser_shoot_time >= self.cooldown_duration:
            self.can_shoot = True
            
        
    def update(self, dt):

        keys =  pygame.key.get_pressed()
        
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])#htis successfully replaces the above code
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        self.direction = self.direction.normalize() if self.direction.magnitude() > 0 else self.direction #this stabilises teh speed
        self.rect.center = self.rect.center +  self.direction * self.speed * dt #multipllying with dt makes the movement speed independent from fps

            #laser
        k = pygame.key.get_just_pressed()
        if k[pygame.K_SPACE] and self.can_shoot:
            Laser(laser_surface, self.rect.midtop, all_sprites)
            self.can_shoot = False
            self.laser_shoot_time = pygame.time.get_ticks()
        
        self.laser_timer()

class Star(pygame.sprite.Sprite):
    def __init__(self, groups , surf):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center=(randrange(0, WIDTH), randrange(0, HEIGHT)))

class Laser(pygame.sprite.Sprite):
    def __init__(self,surf, pos, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=pos)
        self.speed = 400
    def update(self, dt):
        self.rect.centery = self.rect.centery - self.speed * dt
        if self.rect.bottom < 0:
            self.kill()
 
class Meteor(pygame.sprite.Sprite):
    def __init__(self, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(midbottom=(randrange(0 , WIDTH), 0))
        self.speed = 200
        self.live = True
        self.birth = pygame.time.get_ticks()
        self.lifetime = 2000 #this is two seconds
        print("created at " , self.birth)
        
    def meteor_timer(self):
        if not self.live:
            return
        if pygame.time.get_ticks() - self.birth >= self.lifetime:
            self.live = False
    def update(self, dt):
        #movement of a meteor
        self.rect.bottom = self.rect.bottom + self.speed * dt
        self.meteor_timer()
        if not self.live:
            self.kill()
            print("killed at" , pygame.time.get_ticks())
    
        
        
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
star_surface = pygame.image.load(join('spaceshift','images', 'star.png')).convert_alpha()
for i in range (20):
    star = Star(all_sprites, star_surface)

player = Player(all_sprites)

meteor_surface = pygame.image.load(join('spaceshift', 'images', 'meteor.png')).convert_alpha()

laser_surface = pygame.image.load(join('spaceshift', 'images', 'laser.png')).convert_alpha()

#custom event -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500) #it will be triggered every 500 miliseconds, twice in a second

while not exit:
    delta_time = clock.tick(120) / 1000 #delta time measrures hte time took by the computer to render in between the last 2 frames, how much time has changed since the last 2 frames, different in everty computer
    for event in pygame.event.get(): #this gets all the events in the pygame
        if event.type == pygame.QUIT:
            exit = True
        if event.type == meteor_event:
            Meteor(meteor_surface , all_sprites)
            pass
         
    all_sprites.update(delta_time)
    keys = pygame.key.get_pressed()
    

    display_surface.fill('darkgrey')#if you remove htis line it does not claer
      
    
    all_sprites.draw(display_surface)
    pygame.display.update()

#ensures that the game will close properly, safety net
pygame.quit()