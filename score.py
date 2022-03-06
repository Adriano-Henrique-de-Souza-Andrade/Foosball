import pygame
from config import SCREEN_SIZE, SCREEN_HEIGHT, SCREEN_WIDTH

class Score():
    pontos_1 = 0
    pontos_2 = 0

    def player_1(self):
        self.pontos_1 += 1
        return self.pontos_1

    def player_2(self):
        self.pontos_2 += 1
        return self.pontos_2

    def placar(self):
        screen = pygame.display.set_mode(SCREEN_SIZE)
        score_font = pygame.font.Font('PressStart2P.ttf', 30)
        score_text = score_font.render('00 x 00', True, "white", "black")
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (480, 30)
        score_text = score_font.render(str(self.pontos_1) + ' x ' + str(self.pontos_2), True, "white", "black")
        screen.blit(score_text, score_text_rect)

        if self.pontos_1 == 7:
            font = pygame.font.Font("fonts/Pixeled.ttf", 70)
            text = font.render("GAME OVER - Player 1 Wins", 1, (255,255,255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5))
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.wait(2000)
            run = False
        if self.pontos_2 == 7:
            font = pygame.font.Font("fonts/Pixeled.ttf", 70)
            text = font.render("GAME OVER - Player 2 Wins", 1, (255,255,255))
            text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 1.5))
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.wait(2000)
            run = False