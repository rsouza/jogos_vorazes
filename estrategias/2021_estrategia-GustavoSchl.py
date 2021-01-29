# Estratégia Jogos Vorazes - Python Verão 2021
# Gustavo Schlemper

from estrategias.jogadores import Jogador

import numpy as np

class MeuJogador(Jogador):

    def __init__(self):
        self.name = "GustavoSchl"

# Para a elaboração da estratégia, poderia utilizar a simetria do jogo. Porém, como a estrategia "caçar" é
# estritamente dominada por "descançar", não importando qual seja a estimativa da probabilidade de que o outro caçe,
# resolvi criar uma estratégia um tanto quanto aleatória

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_jogadores):

        if rodada <= 5:
            escolha = [np.random.choice(['c','d']) for i in range(len(reputacoes_jogadores))]

        else:
            escolha = []

            for reputacao in reputacoes_jogadores:

                if 0.4 <= reputacao <=0.6:
                    escolha.append(np.random.choice(['c','d']))

                elif reputacao <0.4:
                    escolha.append('d')

                else:
                    escolha.append('c')

        return escolha


