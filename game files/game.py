import pygame

import config
from screen import draw, ScreenMulti, ScreenSelection, ScreenSingle
from config import pause, TRANSITION_TIME, INITIAL_PLAYERS_COORD
from colors import Colors


def comands_verifying():
    global pause
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False
        elif event.type == pygame.KEYDOWN:
            pause = not pause


def select_mode():
    count = 0
    quiting_time = -100

    while config.selecting and config.playing:
        screen_count = count
        if(quiting_time > 0):
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

    while config.single and config.playing:
        draw("Evolution Foosball sp- LPC", INITIAL_PLAYERS_COORD, (count, 276), pause)
        comands_verifying()
        count+=aux
        if count > 500 or count < 300:
            aux*=-1



def game_loop_multi():
    while config.multi and config.playing:
        draw("Evolution Foosball mp- LPC", INITIAL_PLAYERS_COORD, (464, 276), pause)
        comands_verifying()
