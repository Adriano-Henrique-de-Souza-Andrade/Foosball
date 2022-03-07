from operator import truediv
from turtle import screensize
import pygame

import config
from ball import Ball
from players import Players
from screen import ScreenSelection, Screen
from config import MAX_GOALS, MULTIPLAYER, SINGLEPLAYER, initial_players_coord, pause, TRANSITION_TIME

pygame.mixer.init()


screen = None
players = None
score = (0, 0)
finished = False


def comands_verifying():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pause = not pause
    if finished:
        pause = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r] and (finished or pause):
        start_game()
    if keys[pygame.K_h] and (finished or pause):
        config.selecting = True
        config.multi = False
        config.single = False
        start_game()
        select_mode()



def select_mode():
    pygame.mixer.music.load("sound/ost/old and classic foosball.mp3")
    pygame.mixer.music.play(-1)

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


def start_game():
    global screen
    global players
    global score
    global pause
    global finished

    Ball.reset(Ball)
    players = Players(SINGLEPLAYER if config.single else MULTIPLAYER)
    screen = Screen("Evolution Foosball " +
                    "sp" if config.single else "mp" + " - LPC")
    score = (0, 0)

    pause = False
    finished = False


def game_loop():
    global screen
    global players
    global score
    global finished

    pygame.mixer.music.load("sound/ost/counting on you.mp3")
    pygame.mixer.music.play(-1)

    start_game()

    while config.playing:

        comands_verifying()

        if not pause and not finished:
            players.move_players()
            Ball.movement(Ball)
            Ball.collision_walls(Ball)
            is_goal = Ball.is_goal(Ball)
            score = (score[0] + is_goal[0], score[1] + is_goal[1])

            if score[0] == MAX_GOALS or score[1] == MAX_GOALS:
                screen.set_finish(
                    "SINGLEPLAYER" if config.single else "MULTIPLATER")
                finished = True

        screen.set_pipes(players.pipe_blmv, players.pipe_rdmv)
        screen.set_players(players.coords)
        screen.set_ball((Ball.ball_rectx, Ball.ball_recty))
        screen.set_column_kicking(Ball.column_kicking)
        screen.set_score(score)

        screen.set_pause(pause)
        screen.draw()
