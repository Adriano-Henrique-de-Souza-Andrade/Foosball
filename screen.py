import pygame
from config import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, TRANSITION_TIME, COLUMN_COLORS, PIPE_WIDTH
from colors import Colors

count = 0
pause_time = -100


def animation_counter(final_value, count, total_frames):
    return final_value - count * (final_value / total_frames)

class Screen:
    surface: pygame.Surface
    player_coords = []
    blue_pipe = 0
    red_pipe = 0
    column_kicking = -1
    count = 0

    pause_start = -100
    pause_end = -100

    result_start = -100
    
    ball_coord = (0, 0)
    score = (0, 0)
    def __init__(self, title):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.surface = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
        pygame.display.set_caption(title)

        self.game_clock = pygame.time.Clock()


        self.floor = pygame.image.load("img/floor.png").convert_alpha()
        self.table = pygame.image.load("img/table.png").convert_alpha()
        self.border = pygame.image.load("img/border.png").convert_alpha()
        self.placar = pygame.image.load("img/placar.png").convert_alpha()
        self.ball = pygame.image.load("img/ball.png").convert_alpha()
        self.pipe_down = pygame.image.load("img/pipe_down.png").convert_alpha()
        self.pipe_up = pygame.image.load("img/pipe_up.png").convert_alpha()
        self.player_red = [
            pygame.image.load("img/player_red.png").convert_alpha(),
            pygame.image.load("img/player_red_kicking_left.png").convert_alpha(),
            pygame.image.load("img/player_red_kicking_right.png").convert_alpha(),
        ]

        self.player_blue = [
            pygame.image.load("img/player_blue.png").convert_alpha(),
            pygame.image.load("img/player_blue_kicking_left.png").convert_alpha(),
            pygame.image.load("img/player_blue_kicking_right.png").convert_alpha(),
        ]
        self.board = pygame.image.load("img/board.png").convert_alpha()


    def set_pipes(self, blue, red):
        self.blue_pipe = blue
        self.red_pipe = red

    def set_players(self, player_coords):
        self.player_coords = player_coords

    def set_score(self, score):
        self.score = score

    def set_ball(self, ball_coord):
        self.ball_coord = ball_coord

    def set_column_kicking(self, column_kicking):
        self.column_kicking = column_kicking

    def set_pause(self, pause):
        if pause:
            if self.pause_start < 0:
                self.pause_start = self.count
            self.pause_end = -100
        else:
            if self.pause_end < 0:
                self.pause_end = self.count
            self.pause_start = -100

    def draw_pipes(self, col_index):
        column = self.player_coords[col_index]

        if COLUMN_COLORS[col_index] == "red":
            self.surface.blit(
                self.pipe_up, (column[0][0] - PIPE_WIDTH / 2, self.red_pipe))
        else:
            self.surface.blit(
                self.pipe_down, (column[0][0] - PIPE_WIDTH / 2, self.blue_pipe))

    def draw_players_column(self, col_index):
        column_state = 0
        column = self.player_coords[col_index]

        if self.column_kicking == col_index:
            if column[0][0] > self.ball_coord[0]:
                column_state = 1
            else:
                column_state = 2

        for position in column:
            if COLUMN_COLORS[col_index] == "red":
                player_position = (
                    position[0] - PLAYER_WIDTH / 2, position[1])
                self.surface.blit(
                    self.player_red[column_state], player_position)
            else:
                player_position = (
                    position[0] - PLAYER_WIDTH / 2, position[1])
                self.surface.blit(
                    self.player_blue[column_state], player_position)

    def draw(self):
        transition = 3

        self.surface.blit(self.floor, (0, 0))
        self.surface.blit(self.table, (75, 60))
        self.surface.blit(self.ball, self.ball_coord)

        for i in range(len(self.player_coords)):
            self.draw_pipes(i)
            self.draw_players_column(i)

        self.surface.blit(self.border, (75, 60))
        self.surface.blit(self.placar, (0, 0))

        animation_count = transition
        if self.pause_start > 0:
            behind = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            behind.set_alpha(animation_count*(128/transition))
            behind.fill(Colors["Black"])

            self.surface.blit(behind, (0, 0))
            self.surface.blit(self.board, (0, animation_counter(-100, animation_count, transition)))

            pygame.draw.rect(self.surface,
                                Colors["White"], [460, 240 + animation_counter(-100, animation_count, transition), 15, 50])
            pygame.draw.rect(self.surface,
                                Colors["White"], [485, 240 + animation_counter(-100, animation_count, transition), 15, 50])

        self.count += 1
        
        pygame.display.flip()
        self.game_clock.tick(60)



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
        multiplayer = font.render(
            "Multiplayer mode", 1, (255, 255, 255)).convert_alpha()
        singleplayer = font.render(
            "Singleplayer mode", 1, (255, 255, 255)).convert_alpha()
        enter_mode = font_enter.render(
            "Press ENTER to start the game", 1, (255, 255, 255)).convert_alpha()

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
