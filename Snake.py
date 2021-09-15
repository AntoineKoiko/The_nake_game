import pygame as pg
import colors
from dimensions import BLOCK_SIZE


class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, win):
        b_sz = BLOCK_SIZE
        x, y = self.x * b_sz, self.y * b_sz

        pg.draw.rect(win, colors.GREEN, (x, y, b_sz, b_sz))


class Snake:
    def __init__(self):
        self.body = [Tile(10, 10), Tile(9, 10)]
        self.direction = 'right'
        self.has_eat = False

    def set_direction(self, direction):
        self.direction = direction
        print(f'new direction {direction}')

    def move(self):
        head = self.body[0]
        head = Tile(head.x, head.y)

        if self.direction == 'right':
            head.x += 1
        if self.direction == 'left':
            head.x -= 1
        if self.direction == 'up':
            head.y -= 1
        if self.direction == 'down':
            head.y += 1
        self.body.insert(0, head)
        if self.has_eat is False:
            self.body.pop()
        self.has_eat = False

    def is_on_body(self, x, y):
        """
        Check if the coordinate are on the snake body
        :param x: x coordinate
        :param y: y coordinate
        :return: True / False depend on the position
        """
        for tile in self.body:
            if tile.x == x and tile.y == y:
                return True
        return False

    def check_apple(self, apple):
        if self.is_on_body(apple.x, apple.y) is True:
            self.has_eat = True
            apple.generate(self)

    def check_body(self, max_x, max_y):
        """
        Check if player loose
        :param max_x: max possible x position
        :param max_y: max possible y position
        :return: True if all good else False
        """
        head = self.body[0]
        for tile in self.body[1:]:
            if head.x == tile.x and head.y == tile.y:
                print('head on body')
                return False
        if head.x < 0 or head.x >= max_x:
            return False
        if head.y < 0 or head.y >= max_y:
            return False
        return True

    def draw(self, win):
        for tile in self.body:
            tile.draw(win)
