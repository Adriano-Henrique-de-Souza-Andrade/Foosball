from operator import truediv
from turtle import screensize
import pygame

import config
from ball import Ball
from players import Players
from screen import ScreenSelection, Screen
from config import  MAX_GOALS, MULTIPLAYER, SINGLEPLAYER, initial_players_coord, pause, TRANSITION_TIME

pygame.mixer.init()
pygame.mixer.music.load("sound/ost/old and classic foosball.mp3")
pygame.mixer.music.play(-1)

screen = None
players = None
score = (0, 0)


def comands_verifying():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pause = not pause

    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        start_game() 

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


def start_game():
    global screen
    global players
    global score
    global pause

    Ball.reset(Ball)
    players = Players(SINGLEPLAYER if config.single else MULTIPLAYER)

    screen = Screen("Evolution Foosball sp- LPC")

    score = (0, 0) 
    pause = False


def game_loop():
    global screen
    global players
    global score

    pygame.mixer.music.load("sound/ost/counting on you.mp3")
    pygame.mixer.music.play(-1)

    start_game()
    
    while config.playing:
        players.move_players()
        comands_verifying()
        
        
        print(initial_players_coord())

        if not pause and  (score[0] < MAX_GOALS or score[1] < MAX_GOALS):

            Ball.movement(Ball)
            Ball.collision_walls(Ball)
            is_goal = Ball.is_goal(Ball)

            score = (score[0] + is_goal[0], score[1] + is_goal[1])

            if score[0] == MAX_GOALS or score[1] == MAX_GOALS:
                screen.set_finish(
                    "SINGLEPLAYER" if config.single else "MULTIPLATER")
                
            comands_verifying()
            screen.set_pipes(players.pipe_blmv, players.pipe_rdmv)
            screen.set_players(players.coords)
            screen.set_ball((Ball.ball_rectx, Ball.ball_recty))
            screen.set_column_kicking(Ball.column_kicking)
            screen.set_score(score)


        screen.set_pause(pause)
        screen.draw()

        
