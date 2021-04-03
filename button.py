from settings import *

class Button():

    settings = Settings()

    def __init__(self, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect = pygame.Rect(0, 0, self.settings.button_width, self.settings.button_height)
        self.rect.center = self.screen_rect.center

        self.prep_message(msg)

    def prep_message(self, msg):
        self.msg_image = self.settings.button_font.render(msg, True, self.settings.button_text_color, self.settings.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)