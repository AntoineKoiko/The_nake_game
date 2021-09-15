#!/usr/bin/env python3
import pygame as pg
import colors
from Snake import Snake
from Apple import Apple
from dimensions import BLOCK_SIZE
pg.font.init()

WIDTH, HEIGHT = 600, 600
WIND = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption('My Snake!!')

FPS = 8

SCORE_FONT = pg.font.SysFont('comicsans', 40)


def draw_window(snake, apple):
    WIND.fill(colors.WHITE)

    score_text = SCORE_FONT.render(f'Health: {len(snake.body) - 2}', 1, colors.BLACK)
    WIND.blit(score_text, (10, 10))

    snake.draw(WIND)
    apple.draw(WIND)

    pg.display.update()


def handle_snake_movement(event, snake):
    if event.key == pg.K_UP and snake.direction != 'down':
        snake.set_direction('up')
    if event.key == pg.K_RIGHT and snake.direction != 'left':
        snake.set_direction('right')
    if event.key == pg.K_DOWN and snake.direction != 'up':
        snake.set_direction('down')
    if event.key == pg.K_LEFT and snake.direction != 'right':
        snake.set_direction('left')


def main():
    running = True
    clock = pg.time.Clock()

    snake = Snake()
    apple = Apple(WIDTH / BLOCK_SIZE, HEIGHT / BLOCK_SIZE)
    apple.generate(snake)

    while running:

        clock.tick(FPS)
        for event in pg.event.get():
            if event.type is pg.QUIT:
                running = False

            if event.type == pg.KEYDOWN:
                handle_snake_movement(event, snake)

        snake.move()
        snake.check_apple(apple)
        if snake.check_body(WIDTH / BLOCK_SIZE, HEIGHT / BLOCK_SIZE) is False:
            running = False
        draw_window(snake, apple)


if __name__ == '__main__':
    main()
