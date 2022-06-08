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
import sys  # for exit
import time
import random


# стартуем в файле модули пайгейм
pygame.init()

# размер окна
display_width = 600  # параметр высоты
display_height = 600  # параметр ширины

# окно игры
gameDisplay = pygame.display.set_mode((display_width, display_height))  # размер
pygame.display.set_caption("Let's crush my car!")  # название

# цвета
black = (0, 204, 204)
white = (238, 204, 204)
red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (255, 0, 0)
bright_red = (255, 0, 0)

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


# счетчик пролетевших блоков
def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Hi, looser, you've reached: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


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


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("Let's crash my car!", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)

        pygame.display.update()
        clock.tick(15)


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

    # тартовое значение для пролетевших блоков
    dodged = 0

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
        thing_starty += thing_speed  # скорость +

        # создаем машину
        car(x, y)
        things_dodged(dodged)

        # задаем границы
        if x > display_width - car_width or x < 0:
            gameExit = True
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            thing_speed += 1
            thing_width += (dodged * 1.005)

        # условия для столкновений с камнями чтобы работали
        if y < thing_starty + thing_height:
            print('y crossover')  # для проверки условия для себя принтим

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        # проверяем на обновления дисплея
        pygame.display.update()
        # кадры в секунду = 60
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
