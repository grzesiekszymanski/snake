from functions import *
from button import Button

settings = Settings()


def main():
    window = pygame.display.set_mode((settings.side, settings.side))
    clock = pygame.time.Clock()
    snake = Snake(settings.snake_color, settings.snake_position)
    meal = Square(settings.meal_color, spawn_meal(settings.rows, snake))
    pygame.display.set_caption("SNAKE")
    play_button = Button(window, "PLAY")
    run_game = False

    while run_game == False:
        show_button(play_button)
        if play(play_button) == True:
            run_game = True
        pygame.display.update()

    while run_game == True:
        clock.tick(12)
        pygame.time.delay(40)

        if snake.snake_body[0].position == meal.position:
            snake.new_square()
            meal = Square(settings.meal_color, spawn_meal(settings.rows, snake))

        for x in range(len(snake.snake_body)):
            if snake.snake_body[x].position in list(map(lambda x:x.position, snake.snake_body[x+1:])):
                print('Your score: ', len(snake.snake_body))
                message_box('You lost', 'Play again')
                snake.new_game(settings.snake_color, settings.snake_position)
                break

        update_screen(window, snake, meal)

main()