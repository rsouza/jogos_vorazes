from estrategias.jogadores import Jogador
import random
import numpy as np

class MeuJogador(Jogador):
    """
    Feito por Lauder Leal
    Caça com metade dos jogadores
    """
    def __init__(self):
        self._name = "Thanos"

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        if rodada == 1:
            for i in range(0,len(reputacoes_dos_jogadores)):
                escolhas.append('c')
        elif rodada < 1000:
            for i in range(0,len(reputacoes_dos_jogadores)):
                if i%4 == 0 or i%4 == 3:
                    escolhas.append('d')
                else:
                    escolhas.append('c')
        else:
            for i in range(0,len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores[i] > 0.7:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        return escolhas
