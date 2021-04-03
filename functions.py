from snake import *
import tkinter
from tkinter import messagebox
import random
settings = Settings()


def update_screen(window, snake, meal):
    window.fill(settings.background_color)
    snake.draw_square(window, settings.snake_color)
    snake.snake_move()
    meal.draw_square(window, settings.meal_color)
    draw_lines(settings.side, settings.rows, window)
    pygame.display.update()

def show_button(play_button):
    play_button.draw_button()
    pygame.display.update()

def play(play_button):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if play_button.rect.collidepoint(mouse_x, mouse_y):
                return True

def spawn_meal(rows, item):
    positions = item.snake_body

    while True:
        x_pos = random.randrange(rows)
        y_pos = random.randrange(rows)
        if len(list(filter(lambda z: z.position == (x_pos, y_pos), positions))) > 0:
            continue
        else:
            break
    return (x_pos, y_pos)

def message_box(subject, content):
    root = tkinter.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass

def draw_lines(side, rows, window):
    distance = settings.side // settings.rows
    x_lines = y_lines = 0

    for row in range(rows):
        x_lines += distance
        y_lines += distance

        pygame.draw.line(window, settings.lines_color, (x_lines, 0), (x_lines, side))
        pygame.draw.line(window, settings.lines_color, (0, y_lines), (side, y_lines))