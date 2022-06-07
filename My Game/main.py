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
import sys
import time
import random

# стартуем в файле модули пайгейм
pygame.init()

# размер окна
display_width = 600  # параметр высоты
display_height = 600  # параметр ширины

# окно игры
gameDisplay = pygame.display.set_mode((display_width, display_height))  # размер
pygame.display.set_caption("Don't crush my car, dude!")  # название

# цвета
black = (0, 204, 204)
white = (238, 204, 204)
red = (255, 0, 0)

# кадры в секунду
clock = pygame.time.Clock()


# player
carImg = pygame.image.load('Image/Blue rodster.png')
carImg = pygame.transform.scale(carImg, (60, 80))
car_width = 70

# функция для появляющихся элементов на дороге
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


# отрисовка авто
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


# обработка текста
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# вывод текста на экран
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(3)

    game_loop()


def crash():
    message_display('GAME OVER!')


# функция для запуска игры
def game_loop():
    # размещение
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    # параметры для появления things
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 8
    thing_width = 60
    thing_height = 60

    x_change = 0  # позиция
    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                pygame.quit()
                sys.exit()

            # блок для обработки нажатия на клавиши
            if event.type == pygame.KEYDOWN:
                # если нажали на esc, то окно закр.
                if event.key == pygame.K_ESCAPE:
                    crashed = True
                    pygame.quit()

                if event.key == pygame.K_LEFT:
                    x_change = -5

                elif event.key == pygame.K_RIGHT:
                    x_change = 5

            # условия для движения
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        # смена позиции
        x += x_change

        # фон
        gameDisplay.fill(white)
        # вызов things
        things(thing_startx, thing_starty, thing_width, thing_height, black)
        thing_starty += thing_speed # скорость +

        # создаем машину
        car(x, y)

        # задаем границы
        if x > display_width - car_width or x < 0:
            gameExit = True
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)

        # проверяем на обновления дисплея
        pygame.display.update()
        # кадры в секунду = 60
        clock.tick(60)


game_loop()
pygame.quit()
quit()


