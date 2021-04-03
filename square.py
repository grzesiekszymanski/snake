import pygame
from settings import Settings


class Square(object):

    settings = Settings()

    def __init__(self, color, start_position):
        self.position = start_position
        self.direction_x = 1
        self.direction_y = 0
        self.color = color

    def move(self, direction_x, direction_y):
        self.direction_x = direction_x
        self.direction_y = direction_y
        self.position = (self.position[0] + self.direction_x, self.position[1] + self.direction_y)

    def draw_square(self, window, color):
        row = self.position[0]
        column = self.position[1]
        distance = self.settings.side // self.settings.rows
        pygame.draw.rect(window, color, (row*distance, column*distance, distance, distance))