import random


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
        if self.ball_recty <= 95:
            self.ball_dy = self.ball_velocity
        if self.ball_recty >= 417:
            self.ball_dy = self.ball_velocity * (-1)
        if self.ball_rectx <= 121 and (self.ball_recty <= 100 or self.ball_recty >= 310):
            self.ball_dx = self.ball_velocity
        if self.ball_rectx >= 812 and (self.ball_recty <= 100 or self.ball_recty >= 310):
            self.ball_dx = self.ball_velocity * (-1)
        # Goal
        if self.ball_rectx <= 121 or self.ball_rectx >= 812:
            self.ball_recty = 260
            self.ball_rectx = 467
        if self.ball_rectx <= 108 or self.ball_rectx >= 830:
            self.ball_recty = 260
            self.ball_rectx = 467
            self.ball_dx = self.ball_velocity * random.sample(self.directions_x, 1)[0]
            self.ball_dy = self.ball_velocity * random.sample(self.directions_y, 1)[0]
