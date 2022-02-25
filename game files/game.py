import pygame

import config
from config import screen_dimensions
from screen import Screen_multi, Screen_selection, Screen_single
from config import pause
from colors import Colors

def comands_verifying():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False
        elif event.type == pygame.KEYDOWN:
            pause = not pause

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
        screen_single = Screen_single(screen_dimensions["width"], screen_dimensions["height"])
        Screen_single.draw(Screen_single)
        comands_verifying()
        if pause is True:
            pygame.draw.rect(screen_single.surface, Colors["White"], [460, 240, 15, 50])
            pygame.draw.rect(screen_single.surface, Colors["White"], [485, 240, 15, 50])
            pygame.display.update()
            continue
        pygame.display.update()


def game_loop_multi():
    while config.multi:
        Screen_multi(screen_dimensions["width"], screen_dimensions["height"])
        screen_multi = Screen_multi(screen_dimensions["width"], screen_dimensions["height"])
        Screen_multi.draw(Screen_multi)
        comands_verifying()
        if pause is True:
            pygame.draw.rect(screen_multi.surface, Colors["White"], [460, 240, 15, 50])
            pygame.draw.rect(screen_multi.surface, Colors["White"], [485, 240, 15, 50])
            pygame.display.update()
            continue
        pygame.display.update()