import pygame


class Screen_single:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Evolution Foosball sp- LPC")


class Screen_multi:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Evolution Foosball mp- LPC")


class Screen_selection:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Tela 1 do jogo")
