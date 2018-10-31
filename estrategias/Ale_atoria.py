
from estrategias.jogadores import Jogador
import random

class MeuJogador(Jogador):

    def __init__(self):
        Jogador.__init__(self)
        self.total_jogador = 0

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []

        for rep in reputacoes_dos_jogadores:
            if rodada == 1:
                 escolhas.append('c')
            else:
                aleatorio = random.randint(0,100)
                if aleatorio >= 50:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        return escolhas

