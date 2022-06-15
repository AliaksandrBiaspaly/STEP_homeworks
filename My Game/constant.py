
from pygame import display, time, image, transform

# размер окна
display_width = 600  # параметр высоты
display_height = 600  # параметр ширины

# окно игры
gameDisplay = display.set_mode((display_width, display_height))  # размер
display.set_caption("Let's crush my car!")  # название

# цвета
# Colors used in project
black = (0, 204, 204)
white = (238, 204, 204)
red = (255, 0, 0)
green = (0, 200, 0)
bright_green = (255, 0, 0)
bright_red = (255, 0, 0)


# кадры в секунду
clock = time.Clock()

# player
carImg = image.load('Image/Blue rodster.png')
carImg = transform.scale(carImg, (60, 80))
car_width = 70
