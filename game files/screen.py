import pygame
from colors import Colors
from config import screen_dimensions, TRANSITION_TIME


def animation_counter(final_value, count, total_frames):
    return final_value - count*(final_value/total_frames)


class Screen_single:
    surface: pygame.Surface

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Evolution Foosball sp- LPC")

    def draw(self):
        screen_single = Screen_single(
            screen_dimensions["width"], screen_dimensions["height"])
        pygame.draw.rect(screen_single.surface,
                         Colors["SaddleBrown"], [0, 0, 960, 60])
        pygame.draw.rect(screen_single.surface,
                         Colors["DarkGray"], [75, 60, 810, 20])
        pygame.draw.rect(screen_single.surface,
                         Colors["SaddleBrown"], [0, 480, 960, 60])
        pygame.draw.rect(screen_single.surface,
                         Colors["DarkGray"], [75, 460, 810, 20])
        pygame.draw.rect(screen_single.surface,
                         Colors["SaddleBrown"], [0, 0, 75, 540])
        pygame.draw.rect(screen_single.surface,
                         Colors["DarkGray"], [75, 60, 25, 400])
        pygame.draw.rect(screen_single.surface,
                         Colors["SaddleBrown"], [885, 0, 75, 540])
        pygame.draw.rect(screen_single.surface,
                         Colors["DarkGray"], [860, 60, 25, 400])
        pygame.draw.rect(screen_single.surface,
                         Colors["Green"], [100, 80, 760, 380])


class Screen_multi:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])
        pygame.display.set_caption("Evolution Foosball mp- LPC")

    def draw(self):
        screen_multi = Screen_single(
            screen_dimensions["width"], screen_dimensions["height"])
        pygame.draw.rect(screen_multi.surface,
                         Colors["SaddleBrown"], [0, 0, 960, 60])
        pygame.draw.rect(screen_multi.surface,
                         Colors["DarkGray"], [75, 60, 810, 20])
        pygame.draw.rect(screen_multi.surface,
                         Colors["SaddleBrown"], [0, 480, 960, 60])
        pygame.draw.rect(screen_multi.surface,
                         Colors["DarkGray"], [75, 460, 810, 20])
        pygame.draw.rect(screen_multi.surface,
                         Colors["SaddleBrown"], [0, 0, 75, 540])
        pygame.draw.rect(screen_multi.surface,
                         Colors["DarkGray"], [75, 60, 25, 400])
        pygame.draw.rect(screen_multi.surface,
                         Colors["SaddleBrown"], [885, 0, 75, 540])
        pygame.draw.rect(screen_multi.surface,
                         Colors["DarkGray"], [860, 60, 25, 400])
        pygame.draw.rect(screen_multi.surface,
                         Colors["Green"], [100, 80, 760, 380])


class Screen_selection:
    def __init__(self, width, height, count):
        if (count < TRANSITION_TIME):
            animation_count = count
        elif count == TRANSITION_TIME:
            animation_count = TRANSITION_TIME+0.2
        else:
            animation_count = TRANSITION_TIME

        self.width = width
        self.height = height
        self.surface = pygame.display.set_mode([width, height])

        grass = pygame.image.load('img/initial_page/grass.png').convert_alpha()
        ball = pygame.image.load(
            'img/initial_page/ball.png').convert_alpha()
        pipes = pygame.image.load('img/initial_page/pipes.png').convert_alpha()
        player_blue = pygame.image.load(
            'img/initial_page/player_blue.png').convert_alpha()
        player1_red = pygame.image.load(
            'img/initial_page/player1_red.png').convert_alpha()
        player2_red = pygame.image.load(
            'img/initial_page/player2_red.png').convert_alpha()
        black_layer = pygame.image.load(
            'img/initial_page/black_bg.png').convert_alpha()

        title = pygame.image.load('img/initial_page/title.png').convert_alpha()

        self.surface.blit(grass, (0, 0))
        self.surface.blit(pipes, (0, 0))
        self.surface.blit(
            ball, (animation_counter(-50, animation_count, TRANSITION_TIME),
                   animation_counter(-50, animation_count, TRANSITION_TIME)))
        self.surface.blit(
            player_blue, (0,  animation_counter(-100, animation_count, TRANSITION_TIME)))
        self.surface.blit(
            player1_red, (0, animation_counter(100, animation_count, TRANSITION_TIME)))
        self.surface.blit(
            player2_red, (0,  animation_counter(100, animation_count, TRANSITION_TIME)))
        self.surface.blit(
            black_layer, (animation_counter(200, animation_count, TRANSITION_TIME), 0))
        self.surface.blit(
            title, (0, animation_counter(-400, animation_count, TRANSITION_TIME)))

        pygame.display.set_caption("Tela 1 do jogo")
        pygame.display.flip()
