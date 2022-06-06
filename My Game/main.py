'''import pygame
import sys
from pygame.color import THECOLORS

pygame.init()
#создание экрана
screen = pygame.display.set_mode((800, 800))
#screen.fill(THECOLORS['aquamarine'])
bg = pygame.image.load('Image/34.png')
bg = pygame.transform.scale(bg, (800, 800))
screen.blit(bg, (10, 10))


r = pygame.Rect(240, 50, 390, 100)
pygame.draw.rect(screen, (50, 50, 250), r, 0)

image = pygame.image.load('Image/11.png')
#image = transparent_back('Image/11.png')
screen.blit(image, (150,200))

r = pygame.Rect(240, 150, 390, 100)
pygame.draw.rect(screen, (255, 255, 0), r, 0)

r = pygame.Rect(250, 250, 10, 180)
pygame.draw.rect(screen, (50, 50, 250), r, 0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()'''

import pygame

# start in module python file
pygame.init()

# display resolution
display_width = 800
display_height = 600

# play window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Don't crush my car")  # Name of game

# colors
black = (0, 0, 0)
white = (255, 255, 255)

# FPS
clock = pygame.time.Clock()

# condition of game over
crashed = False

# player
carImg = pygame.image.load('Image/CAR red.png ')
#carImg = pygame.image.transform.scale(carImg, (70, 88))

# drawing car
def car(x, y):
    gameDisplay.blit(carImg, (x, y))

#replacement
x = (display_width * 0.5)
y = (display_height * 0.8)

#start game
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key ==pygame.K_ESCAPE:
                crashed = True
                pygame.quit()
#background
    gameDisplay.fill(white)
#create a car
    car(x, y)
# check update of screen
    pygame.display.update()
    #FPS
    clock.tick(68)

pygame.quit()
sys.exit()

