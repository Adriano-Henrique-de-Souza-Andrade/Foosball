import pygame

import config
from screen import draw, ScreenMulti, ScreenSelection, ScreenSingle
from config import pause, TRANSITION_TIME, INITIAL_PLAYERS_COORD
from colors import Colors

pygame.mixer.init()
pygame.mixer.music.load("sound/ost/old and classic foosball.mp3")
pygame.mixer.music.play(-1)


def comands_verifying():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_p]: 
        #     pause = not pause


def select_mode():
    count = 0
    quiting_time = -100

    while config.selecting and config.playing:
        screen_count = count
        if (quiting_time > 0):
            screen_count = TRANSITION_TIME - (count - quiting_time)
        ScreenSelection(screen_count)
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

    count = 300
    aux = 4

    add_y = -2
    y_axis_mdf = 0
    y_axis_atk = 0
    y_axis_dfd = 0
    pygame.mixer.music.load("sound/ost/counting on you.mp3")
    pygame.mixer.music.play(-1)
    while config.single and config.playing:

        if pygame.key.get_pressed()[pygame.K_w] and add_y > -35:
            add_y -= 3
            y_axis_mdf -= 4
            y_axis_dfd -= 6
            y_axis_atk -= 5
        elif pygame.key.get_pressed()[pygame.K_s] and add_y < 18:
            add_y += 3
            y_axis_mdf += 4
            y_axis_dfd += 6
            y_axis_atk += 5

        y_axis = [y_axis_mdf, y_axis_dfd, y_axis_atk]
        draw("Evolution Foosball sp- LPC", INITIAL_PLAYERS_COORD, (464, 276), add_y, y_axis, -1, pause)
        comands_verifying()
        count += aux
        if count > 500 or count < 300:
            aux *= -1


def game_loop_multi():
    count = 300

    aux = 4
    pygame.mixer.music.load("sound/ost/counting on you.mp3")
    pygame.mixer.music.play()
    while config.multi and config.playing:
        draw("Evolution Foosball mp- LPC", INITIAL_PLAYERS_COORD, (464, 276), -1, pause)
        comands_verifying()