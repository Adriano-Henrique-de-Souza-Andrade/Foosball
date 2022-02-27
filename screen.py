from audioop import mul
import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, TRANSITION_TIME, COLUMN_COLORS, PIPE_WIDTH
from colors import Colors

count = 0
pause_time = -100

def animation_counter(final_value, count, total_frames):
    return final_value - count * (final_value / total_frames)


def draw(caption, player_coords, ball_coord, add_y, y_axis, column_kicking, pause):
    global count
    global pause_time
    self = Screen(caption)
    pygame.display.set_caption(caption)
    floor = pygame.image.load("img/floor.png").convert_alpha()
    table = pygame.image.load("img/table.png").convert_alpha()
    border = pygame.image.load("img/border.png").convert_alpha()
    placar = pygame.image.load("img/placar.png").convert_alpha()
    ball = pygame.image.load("img/ball.png").convert_alpha()
    pipe_down = pygame.image.load("img/pipe_down.png").convert_alpha()
    pipe_up = pygame.image.load("img/pipe_up.png").convert_alpha()
    player_red = [
        pygame.image.load("img/player_red.png").convert_alpha(),
        pygame.image.load("img/player_red_kicking_left.png").convert_alpha(),
        pygame.image.load("img/player_red_kicking_right.png").convert_alpha(),
    ]

    player_blue = [
        pygame.image.load("img/player_blue.png").convert_alpha(),
        pygame.image.load("img/player_blue_kicking_left.png").convert_alpha(),
        pygame.image.load("img/player_blue_kicking_right.png").convert_alpha(),
    ]

    self.surface.blit(floor, (0, 0))
    self.surface.blit(table, (75, 60))
    self.surface.blit(ball, ball_coord)

    for i in range(len(player_coords)):
        column_state = 0
        column = player_coords[i]
        pipe_coord = (column[0][0] - PIPE_WIDTH / 2, add_y)

        if column_kicking == i:
            if column[0][0] > ball_coord[0]:
                column_state = 1
            else:
                column_state = 2

        if COLUMN_COLORS[i] == "red":
            self.surface.blit(pipe_up, (pipe_coord))
        else:
            self.surface.blit(pipe_down, (pipe_coord))

        for position in column:
            if COLUMN_COLORS[i] == "red":
                player_position = (position[0] - PLAYER_WIDTH / 2, position[1])
                self.surface.blit(player_red[column_state], player_position)
            else:
                if i == 1:
                    player_position = (position[0] - PLAYER_WIDTH / 2, position[1] + y_axis[1])
                elif i == 3:
                    player_position = (position[0] - PLAYER_WIDTH / 2, position[1] + y_axis[0])
                else:
                    player_position = (position[0] - PLAYER_WIDTH / 2, position[1] + y_axis[2])
                self.surface.blit(player_blue[column_state], player_position)

    self.surface.blit(border, (75, 60))
    self.surface.blit(placar, (0, 0))

    board = pygame.image.load("img/board.png").convert_alpha()

    animation_count = -1

    if pause is True:
        pause_transition = 3
        if pause_time < 0:
            pause_time = count

        if (count-pause_time < pause_transition):
            animation_count = count-pause_time
        elif count == pause_transition:
            animation_count = pause_transition+0.2
        else:
            animation_count = pause_transition


        behind = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        behind.set_alpha(animation_count*(128/pause_transition))
        behind.fill(Colors["Black"])

        self.surface.blit(behind, (0, 0))
        self.surface.blit(board, (0, animation_counter(-100, animation_count, pause_transition)))

        pygame.draw.rect(self.surface,
                         Colors["White"], [460, 240 + animation_counter(-100, animation_count, pause_transition), 15, 50])
        pygame.draw.rect(self.surface,
                         Colors["White"], [485, 240 + animation_counter(-100, animation_count, pause_transition), 15, 50])
    else:
        pause_time = -100

    count+=1
    pygame.display.update()


class Screen:
    surface: pygame.Surface

    def __init__(self, title):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption(title)


class ScreenSingle:
    surface: pygame.Surface

    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption("Evolution Foosball sp- LPC")


class ScreenMulti:
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption("Evolution Foosball mp- LPC")


class ScreenSelection:
    def __init__(self, count):
        if (count < TRANSITION_TIME):
            animation_count = count
        elif count == TRANSITION_TIME:
            animation_count = TRANSITION_TIME + 0.2
        else:
            animation_count = TRANSITION_TIME

        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

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

        # text selection
        pygame.font.init()

        font = pygame.font.Font("fonts/Pixeled.ttf", 15)
        font_enter = pygame.font.Font("fonts/Pixeled.ttf", 8)
        multiplayer = font.render("Multiplayer mode", 1, (255, 255, 255)).convert_alpha()
        singleplayer = font.render("Singleplayer mode", 1, (255, 255, 255)).convert_alpha()
        enter_mode = font_enter.render("Press ENTER to start the game", 1, (255, 255, 255)).convert_alpha()

        # self.surface.blit(text, (5, 350))
        self.surface.blit(grass, (0, 0))
        self.surface.blit(pipes, (0, 0))
        self.surface.blit(
            ball, (animation_counter(-50, animation_count, TRANSITION_TIME),
                   animation_counter(-50, animation_count, TRANSITION_TIME)))
        self.surface.blit(
            player_blue, (0, animation_counter(-100, animation_count, TRANSITION_TIME)))
        self.surface.blit(
            player1_red, (0, animation_counter(100, animation_count, TRANSITION_TIME)))
        self.surface.blit(
            player2_red, (0, animation_counter(100, animation_count, TRANSITION_TIME)))
        self.surface.blit(
            black_layer, (animation_counter(200, animation_count, TRANSITION_TIME), 0))
        self.surface.blit(
            title, (0, animation_counter(-400, animation_count, TRANSITION_TIME)))
        self.surface.blit(
            singleplayer, (150, animation_counter(400, animation_count / 3, TRANSITION_TIME)))
        self.surface.blit(
            multiplayer, (155, animation_counter(450, animation_count / 3, TRANSITION_TIME)))
        self.surface.blit(
            enter_mode, (155, animation_counter(500, animation_count / 3.5, TRANSITION_TIME)))

        pygame.display.set_caption("Tela 1 do jogo")
        pygame.display.flip()