import pygame

import config
from config import screen_dimensions
from screen import draw, ScreenMulti, ScreenSelection, ScreenSingle
from config import pause, TRANSITION_TIME
from colors import Colors


def comands_verifying():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False
            pygame.display.quit()
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            pause = not pause


def select_mode():
    count = 0
    quiting_time = -100

    while config.selecting:
        screen_count = count
        if(quiting_time>0):
            screen_count = TRANSITION_TIME - (count - quiting_time)
        ScreenSelection(
            screen_dimensions["width"], screen_dimensions["height"], screen_count)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                config.playing = False
                pygame.display.quit()
                pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            quiting_time = count
            config.single = True

        if keys[pygame.K_m]:
            quiting_time = count
            config.multi = True

        if count == quiting_time + TRANSITION_TIME:
            config.selecting = False

        count += 1


def game_loop_single():
    while config.single:
        screen_single = ScreenSingle(
            screen_dimensions["width"], screen_dimensions["height"])
        draw(screen_single)
        comands_verifying()
        if pause is True:
            pygame.draw.rect(screen_single.surface,
                             Colors["White"], [460, 240, 15, 50])
            pygame.draw.rect(screen_single.surface,
                             Colors["White"], [485, 240, 15, 50])
            pygame.display.update()
            continue
        pygame.display.update()


def game_loop_multi():
    while config.multi:
        ScreenMulti(screen_dimensions["width"], screen_dimensions["height"])
        screen_multi = ScreenMulti(
            screen_dimensions["width"], screen_dimensions["height"])
        draw(screen_multi)
        comands_verifying()
        if pause is True:
            pygame.draw.rect(screen_multi.surface,
                             Colors["White"], [460, 240, 15, 50])
            pygame.draw.rect(screen_multi.surface,
                             Colors["White"], [485, 240, 15, 50])
            pygame.display.update()
            continue
        pygame.display.update()
