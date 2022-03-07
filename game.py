import pygame

import config
from ball import Ball
from players import Players
from screen import ScreenSelection, Screen
from config import MULTIPLAYER, SINGLEPLAYER, pause, TRANSITION_TIME, INITIAL_PLAYERS_COORD, COLUMNS_VELOCITY, COLUMN_COLORS

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

def game_loop():
    
    pygame.mixer.music.load("sound/ost/counting on you.mp3")
    pygame.mixer.music.play(-1)

    screen = Screen("Evolution Foosball sp- LPC")
    players = Players(SINGLEPLAYER if config.single else MULTIPLAYER)

    score = (0, 0)


    while config.playing:
        players.move_players()
        comands_verifying()

        if not pause and  (score[0] < 1 or score[1] < 1):

            Ball.movement(Ball)
            Ball.collision_walls(Ball)
            is_goal = Ball.is_goal(Ball)
            score = (score[0] + is_goal[0], score[1] + is_goal[1])

            if score[0] == 1 or score[1] == 1:
                screen.set_finish(
                    "SINGLEPLAYER" if config.single else "MULTIPLATER")
                

            screen.set_pipes(players.pipe_blmv, players.pipe_rdmv)
            screen.set_players(players.coords)
            screen.set_ball((Ball.ball_rectx, Ball.ball_recty))
            screen.set_column_kicking(Ball.column_kicking)
            screen.set_score(score)


        screen.set_pause(pause)
        screen.draw()

        if (config.single and players.game_type == MULTIPLAYER) or (config.multi and players.game_type == SINGLEPLAYER):
            screen = Screen("Evolution Foosball sp- LPC")
            players = Players(SINGLEPLAYER if config.single else MULTIPLAYER)

            score = (0, 0)