import pygame

class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Evolution Foosball - LPC")
