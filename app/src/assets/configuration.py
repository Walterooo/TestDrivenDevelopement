from pygame import Color

""" Configuration """
SCREEN_SIZE = WIDTH, HEIGHT = (600, 600)

CELLS_PER_WIDTH = 100
CELLS_PER_HEIGHT = 100
COUNT_OF_CELLS = 50  # I DONT LIKE THIS

CELLS_SIZE_WIDTH = int(WIDTH / COUNT_OF_CELLS)
CELLS_SIZE_HEIGHT = int(HEIGHT / COUNT_OF_CELLS)

BACKGROUND = Color(0, 0, 0)
COLOR_CELL_ALIVE = Color(255, 255, 255)
COLOR_CELL_DEAD = Color(0, 0, 0)

# FPS = 100
