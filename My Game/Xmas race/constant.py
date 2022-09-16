import pygame
from pygame import display, time, image, transform
from os import path
from pygame import mixer

from pygame.mixer import Sound

# размер окна
display_width = 800  # параметр высоты
display_height = 600  # параметр ширины

# окно игры
gameDisplay = display.set_mode((display_width, display_height))  # размер
display.set_caption("Xmas race")  # название

# цвета
# Colors used in project
black = (0, 204, 204)
white = (108, 130, 133)
red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (255, 0, 0)
bright_red = (255, 0, 0)

# кадры в секунду
clock = time.Clock()

# player1
carImg = image.load('Image/red-car.png')
carImg = transform.scale(carImg, (60, 100))
car_width = 60

# player2
car2Img = image.load('Image/police transparent.png')
car2Img = transform.scale(car2Img, (100, 100))
car2_width = 60

# dodge
thingImg = image.load('Image/snowman-with-christmas-lantern-png-download-free.png')
thingImg = transform.scale(thingImg, (80, 80))

thing2Img = image.load('Image/girl-christmas-free-download-image.png')
thing2Img = transform.scale(thing2Img, (90, 100))
thing2_width = 60

snd_dir = path.join(path.dirname(__file__), 'snd')
pygame.init()
intro_sound = Sound(path.join('Sounds/destiny.wav'))
race_sound = Sound(path.join('Sounds/dizzy_racing.ogg'))
crash_sound = Sound(path.join('Sounds/carcrash.wav'))
