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

    def movement(self):
        self.ball_rectx += self.ball_dx
        self.ball_recty += self.ball_dy

    def collision_walls(self):  
        # Goal
        if self.ball_recty >= SCREEN_HEIGHT/2 - 61 and self.ball_recty <= SCREEN_HEIGHT/2 + 61:
            if self.ball_rectx <= 121 or self.ball_rectx >= 812:
                self.ball_recty = 260
                self.ball_rectx = 467
            if self.ball_rectx <= 108 or self.ball_rectx >= 830:
                self.ball_recty = 260
                self.ball_rectx = 467
                self.ball_dx = self.ball_velocity * \
                    random.sample(self.directions_x, 1)[0]
                self.ball_dy = self.ball_velocity * \
                    random.sample(self.directions_y, 1)[0]

        if self.ball_recty <= 95:
            self.ball_dy = self.ball_velocity
        if self.ball_recty >= 417:
            self.ball_dy = self.ball_velocity * (-1)
        if self.ball_rectx <= 121:
            self.ball_dx = self.ball_velocity
        if self.ball_rectx >= 812:
            self.ball_dx = self.ball_velocity * (-1)

    def collision_players(self, players):
        
        for (i, column) in enumerate(players):
            for player in column:
                rect = (int(player[0] - PLAYER_WIDTH/2),  player[1])
                if self.ball_recty + BALL_SIZE >= rect[1] -4 and self.ball_recty <= rect[1] + PLAYER_HEIGHT + 4:
                    if self.ball_rectx + BALL_SIZE >= rect[0] -4 and self.ball_rectx + BALL_SIZE <= rect[0]:
                        self.ball_dx = self.ball_velocity * -1
                        return i
                    elif self.ball_rectx >= rect[0] + PLAYER_WIDTH and self.ball_rectx <= rect[0] + PLAYER_WIDTH +4:
                        self.ball_dx = self.ball_velocity 
                        return i
                    elif self.ball_rectx + BALL_SIZE > rect[0] and self.ball_rectx < rect[0] + PLAYER_WIDTH: 
                        self.ball_dy = self.ball_dy * (-1) 


        return -1
