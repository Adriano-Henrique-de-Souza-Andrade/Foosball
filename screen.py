import pygame
from config import GAME_FONT, MAX_GOALS, SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_WIDTH, TRANSITION_TIME, COLUMN_COLORS, PIPE_WIDTH
from colors import Colors
from ball import Ball

count = 0
pause_time = -100


def animation_counter(final_value, count, total_frames):
    return final_value - count * (final_value / total_frames)

def center_in_screen (width):
    return (SCREEN_WIDTH - width)/2

class Screen:
    surface: pygame.Surface
    player_coords = []
    blue_pipe = 0
    red_pipe = 0
    column_kicking = -1
    count = 0

    panel_start = -100
    panel_end = -100

    result_start = -100
    
    ball_coord = (0, 0)

    is_paused = False
    is_finished = False

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
        self.title = pygame.font.Font(GAME_FONT, 30)
        self.text = pygame.font.Font(GAME_FONT, 10)

        self.is_finished = False
        self.score = (0, 0)
        self.panel_start = -100

    def set_pipes(self, blue, red):
        self.blue_pipe = blue
        self.red_pipe = red

    def set_players(self, player_coords):
        self.player_coords = player_coords

    def set_score(self, score):
        self.score = score 

    def set_finish(self, type_game):
        self.is_finished = True
        self.type_game = type_game

        if self.panel_start < 0:
            self.panel_start = self.count
        self.panel_end = -100

    def set_ball(self, ball_coord):
        self.ball_coord = ball_coord

    def set_column_kicking(self, column_kicking):
        self.column_kicking = column_kicking

    def set_pause(self, pause):
        if self.is_finished: 
            return
        self.is_paused = pause
        

        if pause:
            if self.panel_start < 0:
                self.panel_start = self.count
        else:
            self.panel_start = -100

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
        

        self.surface.blit(self.floor, (0, 0))
        self.surface.blit(self.table, (75, 60))
        self.surface.blit(self.ball, self.ball_coord)


        for i in range(len(self.player_coords)):
            self.draw_pipes(i)
            self.draw_players_column(i)

        self.surface.blit(self.border, (75, 60))
        self.surface.blit(self.placar, (0, 0))
        score_font = pygame.font.Font("fonts/PressStart2P.ttf", 25)
        score_text = score_font.render(f"{self.score[0]}    {self.score[1]}", True, Colors["White"])
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (480, 30)
        self.surface.blit(score_text, score_text_rect)

        
        if self.panel_start > 0:
            self.draw_panel( "PAUSE" if self.is_paused else "FINISH_GAME" )
            
        self.count += 1
        
        pygame.display.flip()
        self.game_clock.tick(60)

    def draw_panel(self, panel_type):
        transition = 3
        if (self.count - self.panel_start < transition):
            animation_count = self.count - self.panel_start
        elif self.count == transition:
            animation_count = transition + 0.2
        else:
            animation_count = transition

        text_title = ""
        text_one = ""
        text_two = ""
        text_three = ""

        if panel_type == "PAUSE":
            text_title = "GAME PAUSED"
            text_one = "CLICK TO RETURN"
            text_two = "PRESS R TO RESTART GAME"
            text_three = "PRESS H TO RETURN TO HOMEPAGE"

        elif panel_type == "FINISH_GAME": 
            if self.score[0] == MAX_GOALS:
                text_title = "YOU WIN" if self.type_game == "SINGLEPLAYER" else "PLAYER 1 WON!"
            elif self.score[1] == MAX_GOALS:
                text_title = "YOU LOOSE" if self.type_game == "SINGLEPLAYER" else "PLAYER 2 WON!"

            text_one = "PRESS R TO PLAY AGAIN"
            text_two = "PRESS H TO RETURN TO HOMEPAGE"
        
        title = self.title.render(text_title, False, (Colors["White"]))

        one = self.text.render(text_one, False, (Colors["White"]))
        two = self.text.render(text_two, False, (Colors["White"]))
        three = self.text.render(text_three, False, (Colors["White"]))

        behind = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        behind.set_alpha(animation_count*(128/transition))
        behind.fill(Colors["Black"])

        self.surface.blit(behind, (0, 0))
        self.surface.blit(self.board, (0, animation_counter(-100, animation_count, transition)))

        self.surface.blit(title, (center_in_screen(title.get_width()), 150 + animation_counter(-100, animation_count, transition)))  
        self.surface.blit(one, (center_in_screen(one.get_width()), 280 + animation_counter(-100, animation_count, transition)))  
        self.surface.blit(two, (center_in_screen(two.get_width()),300 + animation_counter(-100, animation_count, transition)))  
        self.surface.blit(three, (center_in_screen(three.get_width()),320 + animation_counter(-100, animation_count, transition)))  



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
        multiplayer = font.render(
            "Multiplayer mode - Press M", False, (Colors["White"])).convert_alpha()
        singleplayer = font.render(
            "Singleplayer mode - Press S", False, (Colors["White"])).convert_alpha()

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
            singleplayer, (160, animation_counter(400, animation_count / 3, TRANSITION_TIME)))
        self.surface.blit(
            multiplayer, (165, animation_counter(450, animation_count / 3, TRANSITION_TIME)))
        pygame.display.set_caption("Tela 1 do jogo")
        pygame.display.flip()
