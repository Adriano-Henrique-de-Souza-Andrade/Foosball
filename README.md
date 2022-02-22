# Evolution Foosball
Um jogo de futebol de mesa(pebolim) desenvolvido pelos alunos da Universidade do Estado do Amazonas, do curso de Sistemas de Informação.
Desenvolvedores: Adriano Henrique, Fernando Freires, Guilherme Santos, Guilherme Tapajós, Larry Amaral e Monike Freitas.
  # Tela do jogo
  De modo geral, há três telas no game:
  1. Tela de início: onde o jogo é introduzido e é possível escolher se este será em single ou em multiplayer.
  2. Tela principal: onde o jogo efetivamente acontece e os controles e comandos são executados.
  3. Tela de pause: exibida após um dos player apertar alguma tecla específica, esta denota, de algum modo, que a partida está pausada.
  4. Tela de vitória: exibe alguma mensagem que afirma a vitória do player contra o computador, do player 1 contra o player 2 e vice-versa.
  5. Tela de derrota: exibe alguma mensagem que afirma a derrota do player caso ele esteja jogando contra o computador.
  
  # Personagem e sua movimentação
  Os personagens são os pequenos jogadores em campo(10 para cada player). O players terão jogadores de cores diferentes.
  A movimentação destes ocorre de maneira simultânea, ou seja, caso um deles se movimente, os outros o acompanharão para o mesmo sentido e a mesma direção.
  
  # Controles e eventos
  De maneira específica, as teclas serão definidas: opções pressionadas pelo mouse na tela inicial para selecionar as especificações da partida e iniciá-la;
                                                    uma para movimentar os jogadores para cima e outra, para baixo(4 teclas exercem essas funções no multiplayer);
                                                    uma tecla para pausar o jogo em singleplayer e duas, em multiplayer;
                                                    uma tecla para reiniciar partida após derrota ou vitória e uma para sair do jogo.
  Eventos: fazer gol, chutar a bola com o jogador, bater a bola na parede, ganhar, perder, pausar a partida, sair do jogo e especificar a partida
  (certos eventos serão acompanhados por aúdios).
  
  # Mecânicas
  1. O jogador rebate a bola para o lado oposto do respectivo gol.
  2. A bola rebate quando entra em contato com alguma das paredes da arena.
  3. Incremento no score e decremento na quantidadde de "vidas/bolas" restante.
  4. Jogadores movem-se, apesar de estarem em posições diferentes, em mesmo número de pixels.
  5. Após um gol, a bola reinicia no meio de campo.
  6. O player que fizer 7 gols é o vencedor.
                                                    
                                                    
     
