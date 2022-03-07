SCREEN_WIDTH = 960
SCREEN_HEIGHT = 540
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
PIPE_WIDTH = 28
BALL_SIZE = 26
PLAYER_HEIGHT = 48
PLAYER_WIDTH = 28
PLAYER_WIDTH_KICKING = 37
single = False
multi = False
selecting = True
pause = False
playing = True
TRANSITION_TIME = 5
GAME_FONT = "fonts/Pixeled.ttf"
COLUMN_COLORS = ['blue', 'blue', 'red', 'blue', 'red', 'blue', 'red', 'red']
COLUMNS_VELOCITY = [5, 6, 6, 4, 4, 6, 6, 5]

MULTIPLAYER = 2
SINGLEPLAYER = 1

MAX_GOALS = 3


def initial_players_coord():
    return [[(153, 257)], [(248, 170), (248, 343)], [(341, 149), (341, 257), (341, 365)], [(434, 125), (434, 213), (434, 301), (434, 389)], [
        (527, 125), (527, 213), (527, 301), (527, 389)], [(620, 149), (620, 257), (620, 365)], [(713, 170), (713, 343)], [(808, 257)]]
