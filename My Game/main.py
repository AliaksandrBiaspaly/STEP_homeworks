import pygame
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
        pygame.display.flip()
