
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
                media = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
                if media > 0.8:
                    escolhas.append('c')
                if media < 0.3:
                    escolhas.append('d')
                if media < 0.8 or media > 0.3:
                    aleatorio = random.randint(0,100)
                    if aleatorio >= 50:
                        escolhas.append('c')
                    else:
                        escolhas.append('d')
        return escolhas