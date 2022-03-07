import pygame
from ball import Ball
from config import COLUMN_COLORS, COLUMNS_VELOCITY, INITIAL_PLAYERS_COORD, SINGLEPLAYER


class Players:
    coords = INITIAL_PLAYERS_COORD
    pipe_blmv = -2
    pipe_rdmv = -2
    blue_direction = 0
    red_direction = 0

    def __init__(self, game_type):
        self.game_type = game_type

    def move_blue(self):
        if pygame.key.get_pressed()[pygame.K_w] and self.pipe_blmv > -35:
            self.blue_direction = -1

        elif pygame.key.get_pressed()[pygame.K_s] and self.pipe_blmv < 18:
            self.blue_direction = 1
        self.pipe_blmv += 3 * self.blue_direction

    def move_red(self):
        if self.game_type == SINGLEPLAYER:
            if self.pipe_rdmv + 100 > Ball.ball_recty and self.pipe_rdmv > -35:
                self.red_direction = -1

            elif self.pipe_rdmv + 270 < Ball.ball_recty and self.pipe_rdmv < 18:
                self.red_direction = 1
            self.pipe_rdmv += 3 * self.red_direction
        else:
            if pygame.key.get_pressed()[pygame.K_UP] and self.pipe_rdmv > -35:
                self.red_direction = -1

            if pygame.key.get_pressed()[pygame.K_DOWN] and self.pipe_rdmv < 18:
                self.red_direction = 1
            self.pipe_rdmv += 3 *self. red_direction

    def move_players(self):
        self.blue_direction = 0
        self.red_direction = 0
        
        self.move_blue()
        self.move_red()

        for i, column in enumerate(self.coords):
            for j, player in enumerate(column):
                if COLUMN_COLORS[i] == "blue":
                    self.coords[i][j] = (
                        player[0], player[1] + COLUMNS_VELOCITY[i] * self.blue_direction)
                if COLUMN_COLORS[i] == "red":
                    self.coords[i][j] = (
                        player[0], player[1] + COLUMNS_VELOCITY[i] * self.red_direction)

                Ball.collision_player(Ball, self.coords[i][j], i)