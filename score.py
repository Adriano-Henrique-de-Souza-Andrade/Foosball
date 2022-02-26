import pygame


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
        score_font = pygame.font.Font('PressStart2P.ttf', 30)
        score_text = score_font.render('00 x 00', True, "white", "black")
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (480, 30)
        score_text = score_font.render(str(self.pontos_1) + ' x ' + str(self.pontos_2), True, "white", "black")
        screen.blit(score_text, score_text_rect)