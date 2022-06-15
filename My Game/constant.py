
from pygame import display, time, image, transform

# размер окна
display_width = 800  # параметр высоты
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

# player1
carImg = image.load('Image/red car.png')
carImg = transform.scale(carImg, (50, 80))
car_width = 70

# player2
car2Img = image.load('Image\police transparent.png')
car2Img = transform.scale(car2Img, (80, 80))
car2_width = 70
