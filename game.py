import pygame

import config
from ball import Ball
from screen import ScreenSelection, Screen
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
    pipe_blmv = -2
    pipe_rdmv = -2
    pygame.mixer.music.load("sound/ost/counting on you.mp3")
    pygame.mixer.music.play(-1)
    screen = Screen("Evolution Foosball sp- LPC")
    score = (0, 0)
    while config.single and config.playing:
        red_direction = 0
        blue_direction = 0
        if pygame.key.get_pressed()[pygame.K_w] and pipe_blmv > -35:
            blue_direction = -1

        elif pygame.key.get_pressed()[pygame.K_s] and pipe_blmv < 18:
            blue_direction = 1
        pipe_blmv += 3 * blue_direction

        if pipe_rdmv + 210 > Ball.ball_recty and pipe_rdmv > -35:
            red_direction = -1

        elif pipe_rdmv + 310 < Ball.ball_recty and pipe_rdmv < 18:
            red_direction = 1
        pipe_rdmv += 3 * red_direction

        for i, column in enumerate(players_coord):
            for j, player in enumerate(column):
                if COLUMN_COLORS[i] == "blue":
                    players_coord[i][j] = (
                        player[0], player[1] + COLUMNS_VELOCITY[i] * blue_direction)
                if COLUMN_COLORS[i] == "red":
                    players_coord[i][j] = (
                        player[0], player[1] + COLUMNS_VELOCITY[i] * red_direction)
                Ball.collision_player(Ball, players_coord[i][j], i)

        comands_verifying()
        Ball.movement(Ball)
        Ball.collision_walls(Ball)
        is_goal = Ball.is_goal(Ball)
        score = (score[0] + is_goal[0], score[1] + is_goal[1])
        
        screen.set_pipes(pipe_blmv, pipe_rdmv)
        screen.set_players(players_coord)
        screen.set_ball((Ball.ball_rectx, Ball.ball_recty))
        screen.set_column_kicking(Ball.column_kicking)
        screen.set_score(score)
        screen.set_pause(pause)
        screen.draw()
        while pause and config.playing:
            comands_verifying()
            screen.draw()
            screen.set_pause(pause)


def game_loop_multi():
    players_coord = INITIAL_PLAYERS_COORD
    pipe_blmv = -2
    pipe_rdmv = -2
    pygame.mixer.music.load("sound/ost/counting on you.mp3")
    pygame.mixer.music.play(-1)
    score = (0, 0)
    screen = Screen("Evolution Foosball mp- LPC")

    while config.multi and config.playing:
        blue_direction = 0
        red_direction = 0
        if pygame.key.get_pressed()[pygame.K_w] and pipe_blmv > -35:
            blue_direction = -1

        if pygame.key.get_pressed()[pygame.K_s] and pipe_blmv < 18:
            blue_direction = 1
        pipe_blmv += 3 * blue_direction

        if pygame.key.get_pressed()[pygame.K_UP] and pipe_rdmv > -35:
            red_direction = -1

        if pygame.key.get_pressed()[pygame.K_DOWN] and pipe_rdmv < 18:
            red_direction = 1
        pipe_rdmv += 3 * red_direction

        for i, column in enumerate(players_coord):
            for j, player in enumerate(column):
                if COLUMN_COLORS[i] == "blue":
                    players_coord[i][j] = (
                        player[0], player[1] + COLUMNS_VELOCITY[i] * blue_direction)
                if COLUMN_COLORS[i] == "red":
                    players_coord[i][j] = (
                        player[0], player[1] + COLUMNS_VELOCITY[i] * red_direction)
                Ball.collision_player(Ball, players_coord[i][j], i)

        comands_verifying()
        Ball.movement(Ball)
        Ball.collision_walls(Ball)
        is_goal = Ball.is_goal(Ball)
        score = (score[0] + is_goal[0], score[1] + is_goal[1])
        
        screen.set_pipes(pipe_blmv, pipe_rdmv)
        screen.set_players(players_coord)
        screen.set_ball((Ball.ball_rectx, Ball.ball_recty))
        screen.set_column_kicking(Ball.column_kicking)
        screen.set_score(score)
        screen.set_pause(pause)
        screen.draw()
        while pause and config.playing:
            comands_verifying()
            screen.draw()
            screen.set_pause(pause)
