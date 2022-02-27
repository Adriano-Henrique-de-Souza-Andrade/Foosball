import pygame

import config
from screen import draw,  ScreenSelection
from config import pause, TRANSITION_TIME, INITIAL_PLAYERS_COORD, COLUMNS_VELOCITY, COLUMN_COLORS

pygame.mixer.init()
pygame.mixer.music.load("sound/ost/old and classic foosball.mp3")
pygame.mixer.music.play(-1)


def comands_verifying():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pause = not pause


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
    players_coord = INITIAL_PLAYERS_COORD

    add_y = -2
    blue_direction = 0
    pygame.mixer.music.load("sound/ost/counting on you.mp3")
    pygame.mixer.music.play(-1)
    while config.single and config.playing:
        blue_direction = 0
        if pygame.key.get_pressed()[pygame.K_w] and add_y > -35:
            blue_direction = -1

        elif pygame.key.get_pressed()[pygame.K_s] and add_y < 18:
            blue_direction = 1
        add_y += 3 * blue_direction

        for i, column in enumerate(players_coord):
            for j, player in enumerate(column):
                if COLUMN_COLORS[i] == "blue":
                    players_coord[i][j] = (
                        player[0], player[1] + COLUMNS_VELOCITY[i] * blue_direction)

        draw("Evolution Foosball sp- LPC", players_coord,
             (464, 276), add_y, 0, -1, pause)
        comands_verifying()


def game_loop_multi():
    count = 300

    aux = 4
    pygame.mixer.music.load("sound/ost/counting on you.mp3")
    pygame.mixer.music.play()
    while config.multi and config.playing:
        draw("Evolution Foosball mp- LPC",
             INITIAL_PLAYERS_COORD, (464, 276), -1, pause)
        comands_verifying()
