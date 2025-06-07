import pygame
from code.Menu import Menu
from code.Const import WIN_WIDHT, WIN_HEIGHT


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))


        while True:
            menu = Menu(self.window)
            menu.run()
            pass


