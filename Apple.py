import random
import pygame as pg
from dimensions import BLOCK_SIZE
import colors


class Apple:
    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.x = 0
        self.y = 0

    def generate(self, snake):
        valid = False
        x, y = 0, 0
        while not valid:
            x = random.randint(0, self.max_x)
            y = random.randint(0, self.max_y)
            if not snake.is_on_body(x, y):
                valid = True
        self.x, self.y = x, y

    def draw(self, win):
        x, y = self.x * BLOCK_SIZE, self.y * BLOCK_SIZE
        x, y = x + BLOCK_SIZE/2, y + BLOCK_SIZE/2
        radius = BLOCK_SIZE/2
        pg.draw.circle(win, colors.RED, (x, y), radius)
