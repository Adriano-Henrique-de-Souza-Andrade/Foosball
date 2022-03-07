import pygame

import game

pygame.init()
game.comands_verifying()
game.select_mode()
game.game_loop()
# game.game_loop_multi()
pygame.display.quit()
pygame.quit()
