import pygame
from os.path import join
from random import randrange, uniform

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
            Laser(laser_surface, self.rect.midtop, (all_sprites, laser_sprites))
            laser_sound.play()
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
        self.original_image = surf
        self.rotation_angle = 0
        self.rotation_speed = randrange(-120 , 150)
        self.rect = self.image.get_frect(midbottom=(randrange(0 , WIDTH), 0))
        self.speed = randrange(250, 550)
        self.live = True
        self.birth = pygame.time.get_ticks()
        self.lifetime = 3000 #this is two seconds
        self.direction = pygame.Vector2(uniform(-0.8 , 0.8) , 1)#so that the meteors do not move in a straight line
        
    def meteor_timer(self):
        if not self.live:
            return
        if pygame.time.get_ticks() - self.birth >= self.lifetime:
            self.live = False
    def update(self, dt):
        #movement of a meteor
        self.rotation_angle = (self.rotation_angle + self.rotation_speed * dt ) % 360
        self.rect.center = self.rect.center + self.speed * self.direction.normalize() * dt
        self.image = pygame.transform.rotozoom(self.original_image, self.rotation_angle, 1)
        self.rect = self.image.get_frect(center=self.rect.center)
        self.direction.x = uniform(-0.4 , 0.4) if randrange(0 , 10) > 7 else self.direction.x
        self.meteor_timer()
        if not self.live:
            self.kill()    

class Explosion(pygame.sprite.Sprite):
    def __init__(self,surfaces :list, pos, groups):
        super().__init__(groups)
        self.surfaces = surfaces
        self.image = surfaces[0] #initial image for the animation
        
        self.rect = self.image.get_frect(center=pos)
        self.animation_speed = 250 #this is in milliseconds
        self.last_image_birth = 0
        self.current_image = 0
        print("initialised the explostion")
    def update(self, dt):
        if pygame.time.get_ticks() - self.last_image_birth >= self.animation_speed * dt:
            self.current_image = self.current_image + 1
            self.last_image_birth = pygame.time.get_ticks()

            print("displaying ", self.current_image)
        
        if self.current_image >= len(self.surfaces):
            self.kill()
            print("killing")
            return 
        
        self.image = self.surfaces[self.current_image]
             
def display_score():
    current_time = int(pygame.time.get_ticks() / 1000) + 1
    text_surf = font.render(str(current_time)  , True, (201 , 170, 250))
    text_rect = text_surf.get_frect(midbottom=(WIDTH / 2, HEIGHT - 20))
    
    pygame.draw.rect(display_surface, (150, 150 , 250), text_rect.inflate(20,16).move(0 , -8) , 5, 5)
    display_surface.blit(text_surf, text_rect)
    
     
pygame.init()

WIDTH, HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("this is the caption")
exit = False

clock = pygame.time.Clock()




all_sprites = pygame.sprite.Group()
meteor_sprites = pygame.sprite.Group()
laser_sprites = pygame.sprite.Group()

star_surface = pygame.image.load(join('spaceshift','images', 'star.png')).convert_alpha()
for i in range (20):
    star = Star(all_sprites, star_surface)

player = Player(all_sprites)
meteor_surface = pygame.image.load(join('spaceshift', 'images', 'meteor.png')).convert_alpha()
laser_surface = pygame.image.load(join('spaceshift', 'images', 'laser.png')).convert_alpha()
font = pygame.font.Font(join('spaceshift', 'images', 'font.ttf'), 30)
explosion_surfaces = []
for i in range(21):
    explosion_surfaces.append(pygame.image.load(join('spaceshift', 'images','explosion', str(i) + '.png')).convert_alpha())

#sound
laser_sound = pygame.mixer.Sound(join('spaceshift', 'audio', 'laser.wav'))
laser_sound.set_volume(0.5)
explosion_sound = pygame.mixer.Sound(join('spaceshift', 'audio', 'explosion.wav'))
damage_sound = pygame.mixer.Sound(join('spaceshift', 'audio', 'damage.ogg'))
game_music = pygame.mixer.Sound(join('spaceshift', 'audio', 'game_music.wav'))
game_music.set_volume(0.3)
game_music.play()

#custom event -> meteor event
meteor_event = pygame.event.custom_type()
pygame.time.set_timer(meteor_event, 500) #it will be triggered every 500 miliseconds, twice in a second



while not exit:
    delta_time = clock.tick(120) / 1000 #delta time measrures hte time took by the computer to render in between the last 2 frames, how much time has changed since the last 2 frames, different in everty computer
    for event in pygame.event.get(): #this gets all the events in the pygame
        if event.type == pygame.QUIT:
            exit = True
        if event.type == meteor_event:
            Meteor(meteor_surface , (all_sprites, meteor_sprites))
    
    #update
    all_sprites.update(delta_time)
    laser = pygame.sprite.groupcollide(meteor_sprites,laser_sprites, True, True)
    
    for collided_stride in laser:
        pos = collided_stride.rect.move(0 , -10).midbottom 
        Explosion(explosion_surfaces, pos, all_sprites)
        explosion_sound.play()
    
    if pygame.sprite.spritecollide(player, meteor_sprites, True, pygame.sprite.collide_mask):
        exit = True
    
    

    display_surface.fill('#3a2e3f')#if you remove htis line it does not claer
    all_sprites.draw(display_surface)
    display_score()
    
    
    pygame.display.update()

#ensures that the game will close properly, safety net
pygame.quit()