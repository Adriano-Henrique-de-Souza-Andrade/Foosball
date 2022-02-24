import pygame

import config
from config import screen_dimensions
from screen import Screen


def comands_verifying():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            config.playing = False


pygame.init()
pygame.mixer.init()

test_sound1 = pygame.mixer.Sound("assets/brick.wav")
test_sound2 = pygame.mixer.Sound("assets/paddle.wav")


def game_loop():
    while config.playing:

        Screen(screen_dimensions["width"], screen_dimensions["height"])
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.K_m:
                test_sound1.play()
