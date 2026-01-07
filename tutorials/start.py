import pygame

pygame.init()

color = (40,49,150)
rect_color = (255,0,0)

position = (0,0)


#canvas creation
canvas = pygame.display.set_mode((500,500))
#canvas title
pygame.display.set_caption("first canvas")
image = pygame.image.load("tutorials/icon.jpg")
exit= False

while not exit:
    canvas.fill(color)
    #canvas.blit(image, dest = position)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.draw.rect(canvas, rect_color, pygame.Rect(200, 150, 100, 50))
    pygame.display.update()
