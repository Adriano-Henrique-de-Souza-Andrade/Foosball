import pygame
from colors import Colors
from config import screen_dimensions

class Screen_single:
    surface: pygame.Surface

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Evolution Foosball sp- LPC")

    def draw(self):
        screen_single = Screen_single(screen_dimensions["width"], screen_dimensions["height"])
        pygame.draw.rect(screen_single.surface, Colors["SaddleBrown"], [0, 0, 960, 60])
        pygame.draw.rect(screen_single.surface, Colors["DarkGray"], [75, 60, 810, 20])
        pygame.draw.rect(screen_single.surface, Colors["SaddleBrown"], [0, 480, 960, 60])
        pygame.draw.rect(screen_single.surface, Colors["DarkGray"], [75, 460, 810, 20])
        pygame.draw.rect(screen_single.surface, Colors["SaddleBrown"], [0, 0, 75, 540])
        pygame.draw.rect(screen_single.surface, Colors["DarkGray"], [75, 60, 25, 400])
        pygame.draw.rect(screen_single.surface, Colors["SaddleBrown"], [885, 0, 75, 540])
        pygame.draw.rect(screen_single.surface, Colors["DarkGray"], [860, 60, 25, 400])
        pygame.draw.rect(screen_single.surface, Colors["Green"], [100, 80, 760, 380])

class Screen_multi:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Evolution Foosball mp- LPC")


    def draw(self):
        screen_multi = Screen_single(screen_dimensions["width"], screen_dimensions["height"])
        pygame.draw.rect(screen_multi.surface, Colors["SaddleBrown"], [0, 0, 960, 60])
        pygame.draw.rect(screen_multi.surface, Colors["DarkGray"], [75, 60, 810, 20])
        pygame.draw.rect(screen_multi.surface, Colors["SaddleBrown"], [0, 480, 960, 60])
        pygame.draw.rect(screen_multi.surface, Colors["DarkGray"], [75, 460, 810, 20])
        pygame.draw.rect(screen_multi.surface, Colors["SaddleBrown"], [0, 0, 75, 540])
        pygame.draw.rect(screen_multi.surface, Colors["DarkGray"], [75, 60, 25, 400])
        pygame.draw.rect(screen_multi.surface, Colors["SaddleBrown"], [885, 0, 75, 540])
        pygame.draw.rect(screen_multi.surface, Colors["DarkGray"], [860, 60, 25, 400])
        pygame.draw.rect(screen_multi.surface, Colors["Green"], [100, 80, 760, 380])

class Screen_selection:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Tela 1 do jogo")

