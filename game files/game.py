import pygame
from screen import Screen
from config import screen_dimensions
import config

def comands_verifying():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False

def game_loop():
    while config.playing:

        Screen(screen_dimensions['width'], screen_dimensions['height'])
        pygame.display.update()
