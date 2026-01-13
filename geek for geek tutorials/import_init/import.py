import pygame
import random

""" (numpass, numfail) = pygame.init()
print("Number of successful initializations:", numpass)
print("Number of failed initializations:", numfail)

 """

pygame.init()
is_initialized = pygame.get_init()
print("Pygame initialized:", is_initialized)

canvas = pygame.display.set_mode((300,300),
                                 pygame.RESIZABLE) #this is width and height the additional argumant checks resizablility
title = "this is the game title"
pygame.display.set_caption(title)
print(type(canvas))
#to keep the window open until the user quits

red = 0
green = 50
blue = 100
color = (red,green,blue)#this is red

#we can get the size of the screen using canvas.get_size()
print("Canvas size:", canvas.get_size())
rup = True
gup = True
bup = True

Icon = pygame.image.load("tutorials/icon.jpg")
pygame.display.set_icon(Icon)
num = 0
exit = False
while not exit:
    num = num + 1
    canvas.fill(color)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
    pygame.draw.circle(canvas, (255,0,0), (150,150), 50)
    if num % 10 == 0:
        list1 = [1 , 2 , 3]
        c = random.choice(list1)
        
        if c == 1:
            green += -1 if gup else 1
            if green >= 255:
                green, gup = 255, True
            elif green <= 10:
                green, gup = 10, False

        elif c == 2:
            blue += -1 if bup else 1
            if blue >= 255:
                blue, bup = 255, True
            elif blue <= 10:
                blue, bup = 10, False

        else:
            red += -1 if rup else 1
            if red >= 255:
                red, rup = 255, True
            elif red <= 10:
                red, rup = 10, False

    color = (red, green , blue)
    pygame.display.flip() #this will update the contents of the canvas, need to execute this to see the effects
