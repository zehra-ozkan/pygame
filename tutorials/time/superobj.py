import pygame

class GameObj:
    
    def __init__(self, width = 10, height=10, color=(255, 255, 255), position=(0, 0)):
        self.width = width
        self.height = height
        self.color = color
        self.position = position
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.position[0], self.position[1], self.width, self.height))
    
    def transposeX(self, delta_x):
        self.position = (self.position[0] + delta_x, self.position[1])
    def transposeY(self, delta_y):
        self.position = (self.position[0], self.position[1] + delta_y)
    
    def collide(self, other) -> bool:
        return (
            self.position[0] < other.position[0] + other.width and
            self.position[0] + self.width > other.position[0] and
            self.position[1] < other.position[1] + other.height and
            self.position[1] + self.height > other.position[1]
        )