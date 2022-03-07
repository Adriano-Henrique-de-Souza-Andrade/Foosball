import random
from config import PLAYER_HEIGHT, PLAYER_WIDTH, BALL_SIZE, SCREEN_HEIGHT


class Ball:
    ball_rectx = 467
    ball_recty = 260
    ball_velocity = 4
    directions_x = [1, -1]
    directions_y = [1, -1]
    ball_dx = ball_velocity * random.sample(directions_x, 1)[0]
    ball_dy = ball_velocity * random.sample(directions_y, 1)[0]

    is_kicking = 0
    column_kicking = -1
    actual_column = -1

    def movement(self):
        self.ball_rectx += self.ball_dx
        self.ball_recty += self.ball_dy

    def is_goal(self):
        goal = (0, 0)
        if self.ball_recty >= SCREEN_HEIGHT/2 - 61 and self.ball_recty <= SCREEN_HEIGHT/2 + 61 and (self.ball_rectx <= 121 or self.ball_rectx >= 812):

            if self.ball_rectx <= 121:
                goal = (0, 1)
            elif self.ball_rectx >= 812:
                goal = (1, 0)

            self.ball_recty = 260
            self.ball_rectx = 467
            self.ball_dx = self.ball_velocity * \
                random.sample(self.directions_x, 1)[0]
            self.ball_dy = self.ball_velocity * \
                random.sample(self.directions_y, 1)[0]

        return goal

    def collision_walls(self):
        
        if self.ball_recty <= 95:
            self.ball_dy = self.ball_velocity
        if self.ball_recty >= 417:
            self.ball_dy = self.ball_velocity * (-1)
        if self.ball_rectx <= 121:
            self.ball_dx = self.ball_velocity
        if self.ball_rectx >= 812:
            self.ball_dx = self.ball_velocity * (-1)

    def collision_player(self, player, column):

        collision = -1
        rect = (int(player[0] - PLAYER_WIDTH/2),  player[1])

        if self.ball_recty + BALL_SIZE >= rect[1] - 4 and self.ball_recty <= rect[1] + PLAYER_HEIGHT - 7:
            if self.ball_rectx + BALL_SIZE >= rect[0] - 4 and self.ball_rectx + BALL_SIZE <= rect[0]:
                self.ball_dx = self.ball_velocity * -1
                collision = column
            elif self.ball_rectx >= rect[0] + PLAYER_WIDTH and self.ball_rectx <= rect[0] + PLAYER_WIDTH + 4:
                self.ball_dx = self.ball_velocity
                collision = column
            elif self.ball_rectx + BALL_SIZE > rect[0] and self.ball_rectx < rect[0] + PLAYER_WIDTH:
                self.ball_dy = self.ball_dy * (-1)

        if column >= self.actual_column and self.column_kicking >= 0:
            self.actual_column = column
            return

        if collision == -1 and self.column_kicking >= 0:
            self.is_kicking += 1

        if self.is_kicking == 4:
            self.is_kicking = 0
            self.column_kicking = collision
        if collision >= 0:
            self.column_kicking = collision
            self.is_kicking = 0
        self.actual_column = column
