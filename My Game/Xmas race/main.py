import pygame
import sys  # for exit
import random
import datetime

from Functions import message_display, button, text_objects, things, car, car2, things_dodged, things2
from constant import *

# стартуем в файле модули пайгейм
pygame.init()
pygame.mixer.init()


def game_intro():
    intro = True

    intro_sound.play()

    while intro:

        for event in pygame.event.get():

            print(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 60)
        TextSurf, TextRect = text_objects("CHRISTMAS RACE", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        gameDisplay.blit(TextSurf, TextRect)

        button("GO!", 150, 450, 100, 50, green, bright_green, game_loop)

        pygame.display.update()
        clock.tick(15)


def crash():
    crash_sound.play()
    race_sound.stop()
    message_display('RED CAR CRASHED!')



def crash_out():
    crash_sound.play()
    race_sound.stop()
    message_display('RED CAR OUT!')


def crash2():
    crash_sound.play()
    race_sound.stop()
    message_display('POLICE LOOSER!')


def crash_girls():
    crash_sound.play()
    race_sound.stop()
    message_display("GIRLS GO TO THE HOSPITAL")


def crash2_out():
    crash_sound.play()
    race_sound.stop()
    message_display('POLICE OUT !')


# функция для запуска игры


def game_loop():
    intro_sound.stop()
    race_sound.play()

    # размещение
    x = (display_width * 0.45)
    y = (display_height * 0.65)

    x1 = (display_width * 0.65)
    y1 = (display_height * 0.8)

    # параметры для появления things
    thing_startx = random.randrange(0, display_width - 50)
    thing_starty = -600
    thing_speed = 4
    thing_width = 60
    thing_height = 70

    thing2_startx = random.randrange(0, display_width - 100)
    thing2_starty = -500
    thing2_speed = 3
    thing2_width = 60
    thing2_height = 70

    # cтартовое значение для пролетевших блоков
    dodged = 0

    x_change = 0
    x1_change = 0  # позиция
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

                if event.key == pygame.K_a:
                    x1_change = -5

                elif event.key == pygame.K_d:
                    x1_change = 5

            # условия для движения
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x1_change = 0

        # смена позиции
        x += x_change
        x1 += x1_change

        # фон
        gameDisplay.fill(white)
        # вызов things
        things(thing_startx, thing_starty)
        thing_starty += thing_speed  # скорость +

        things2(thing2_startx, thing2_starty)
        thing2_starty += thing2_speed  # скорость +

        # создаем машину
        car(x, y)
        car2(x1, y1)
        things_dodged(dodged)

        # задаем границы
        if x > display_width - car_width or x < 0:
            gameExit = True
            crash_out()

        if x1 > display_width - car2_width or x1 < 0:
            gameExit = True
            crash2_out()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width - 100)
            dodged += 1
            thing_speed += 0.9
            # thing_width += (dodged * 1.1)

        if thing2_starty > display_height:
            thing2_starty = 0 - thing2_height
            thing2_startx = random.randrange(0, display_width - 100)
            dodged += 1
            thing2_speed += 0.7

        # условия для столкновений с камнями чтобы работали
        if y < thing_starty + thing_height:
            print('y crossover')  # для проверки условия для себя принтим

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()
        if y < thing2_starty + thing2_height:
            print('y crossover')  # для проверки условия для себя принтим

            if x > thing2_startx and x < thing2_startx + thing2_width or x + car_width > thing2_startx and x + car_width < thing2_startx + thing2_width:
                print('x crossover')
                crash()

        if y1 < thing_starty + thing_height:
            print('y1 crossover')  # для проверки условия для себя принтим

            if x1 > thing_startx and x1 < thing_startx + thing_width or x1 + car2_width > thing_startx and x1 + car2_width < thing_startx + thing_width:
                print('x1 crossover')
                crash2()

        if y1 < thing2_starty + thing2_height:
            print('y1 crossover')  # для проверки условия для себя принтим

            if x1 > thing2_startx and x1 < thing2_startx + thing2_width or x1 + car2_width > thing2_startx and x1 + car2_width < thing2_startx + thing2_width:
                print('x1 crossover')
                crash_girls()

        # проверяем на обновления дисплея
        pygame.display.update()
        # кадры в секунду = 60
        clock.tick(60)


game_intro()
game_loop()
pygame.quit()
quit()
