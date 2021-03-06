import time

from pygame import draw, font, mouse, display


# функция для появляющихся элементов на дороге
from constant import gameDisplay, carImg, black, display_height, display_width, car2Img, thingImg, thing2Img


def things(x, y):
    gameDisplay.blit(thingImg, (x, y))


def things2(x, y):
    gameDisplay.blit(thing2Img, (x, y))


# отрисовка авто
def car(x, y):
    gameDisplay.blit(carImg, (x, y))


def car2(x1, y1):
    gameDisplay.blit(car2Img, (x1, y1))


# счетчик пролетевших блоков
def things_dodged(count):
    font1 = font.SysFont(None, 25)
    text = font1.render("Hi, looser, you've reached: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))


# обработка текста
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


# вывод текста на экран
def message_display(text):
    largeText = font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    display.update()

    time.sleep(3)
    from main import game_loop
    game_loop()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse1 = mouse.get_pos()
    click = mouse.get_pressed()
    print(click)

    if x + w > mouse1[0] > x and y + h > mouse1[1] > y:
        draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()

    else:
        draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)
