import pygame
pygame.init()

class Settings():

    def __init__(self):
        self.side = 700
        self.rows = 20

        self.snake_position = (5, 5)

        self.snake_color = (0, 100, 0)
        self.background_color = (216,191,216)
        self.meal_color = (255, 0, 0)
        self.lines_color = (0, 0, 0)

        self.button_width = 200
        self.button_height = 50
        self.button_color = (0, 255, 0)
        self.button_text_color = (255, 255, 255)
        self.button_font = pygame.font.SysFont(None, 48)