import sys
from square import *
settings = Settings()


class Snake(object):

    change_direction = {}
    snake_body = []

    def __init__(self, color, position):
        self.direction_x = 0
        self.direction_y = 1
        self.color = color
        self.head = Square(color, position)
        self.snake_body.append(self.head)

    def draw_square(self, window, color):
        for index, square in enumerate(self.snake_body):
            square.draw_square(window, color)

    def snake_move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    self.direction_x = 0
                    self.direction_y = -1
                    self.change_direction[self.head.position[:]] = [self.direction_x, self.direction_y]

                elif event.key == pygame.K_DOWN:
                    self.direction_x = 0
                    self.direction_y = 1
                    self.change_direction[self.head.position[:]] = [self.direction_x, self.direction_y]

                elif event.key == pygame.K_RIGHT:
                    self.direction_x = 1
                    self.direction_y = 0
                    self.change_direction[self.head.position[:]] = [self.direction_x, self.direction_y]

                elif event.key == pygame.K_LEFT:
                    self.direction_x = -1
                    self.direction_y = 0
                    self.change_direction[self.head.position[:]] = [self.direction_x, self.direction_y]


        for index, square in enumerate(self.snake_body):
            position = square.position[:]
            if position in self.change_direction:
                turn = self.change_direction[position]
                square.move(turn[0], turn[1])
                if index == len(self.snake_body)-1:
                    self.change_direction.pop(position)
            else:
                if square.direction_x == -1 and square.position[0] <= 0:
                    square.position = (square.settings.rows - 1, square.position[1])
                elif square.direction_x == 1 and square.position[0] >= square.settings.rows - 1:
                    square.position = (0, square.position[1])
                elif square.direction_y == 1 and square.position[1] >= square.settings.rows - 1:
                    square.position = (square.position[0], 0)
                elif square.direction_y == -1 and square.position[1] <= 0:
                    square.position = (square.position[0], square.settings.rows - 1)
                else:
                    square.move(square.direction_x, square.direction_y)

    def new_square(self):
        last_square = self.snake_body[-1]
        dir_x = last_square.direction_x
        dir_y = last_square.direction_y

        if dir_x == 1 and dir_y == 0:
            self.snake_body.append(Square(settings.snake_color, (last_square.position[0] - 1, last_square.position[1])))
        elif dir_x == -1 and dir_y == 0:
            self.snake_body.append(Square(settings.snake_color, (last_square.position[0] + 1, last_square.position[1])))
        elif dir_x == 0 and dir_y == 1:
            self.snake_body.append(Square(settings.snake_color, (last_square.position[0], last_square.position[1] - 1)))
        elif dir_x == 0 and dir_y == -1:
            self.snake_body.append(Square(settings.snake_color, (last_square.position[0], last_square.position[1] + 1)))
        self.snake_body[-1].direction_x = dir_x
        self.snake_body[-1].direction_y = dir_y

    def new_game(self, color, position):
        self.head = Square(color, position)
        self.snake_body = []
        self.snake_body.append(self.head)
        self.change_direction = {}
        self.direction_x = 0
        self.direction_y = 1