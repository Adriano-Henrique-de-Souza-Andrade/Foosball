import pygame
from random import randint

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('img/ball.png')
        self.velocity = [randint(4, 8), randint(-8, 8)]
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def kick(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8, 8)
