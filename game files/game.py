import pygame

import config
from config import screen_dimensions
from screen import Screen_multi, Screen_selection, Screen_single


def comands_verifying():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False


def select_mode():
    while config.selecting:
        Screen_selection(screen_dimensions["width"], screen_dimensions["height"])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.playing = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            config.selecting = False
            config.single = True
            pass

        if keys[pygame.K_m]:
            config.selecting = False
            config.multi = True
            pass


def game_loop_single():
    while config.single:
        Screen_single(screen_dimensions["width"], screen_dimensions["height"])
        pygame.display.update()


def game_loop_multi():
    while config.multi:
        Screen_multi(screen_dimensions["width"], screen_dimensions["height"])
        pygame.display.update()
