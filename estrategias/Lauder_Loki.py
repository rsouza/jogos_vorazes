from estrategias.jogadores import Jogador
import random
import numpy as np

class MeuJogador(Jogador):
    """
    Feito por Lauder Leal
    Ajuda mas trai sempre que possível
    """
    def __init__(self):
        self._name = "Loki"

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        if rodada == 1:
            for i in range(0,len(reputacoes_dos_jogadores)):
                escolhas.append('c')
        else:
            if reputacao_atual > 0.6:
                for i in range(0,len(reputacoes_dos_jogadores)):
                    if reputacoes_dos_jogadores[i] < 0.6 or reputacoes_dos_jogadores[i] >= 0.9:
                        escolhas.append('d')
                    else:
                        if rodada % 20 == 1:
                            escolhas.append('d')
                        else:
                            escolhas.append('c')
            else:
                for i in range(0,len(reputacoes_dos_jogadores)):
                    if reputacoes_dos_jogadores[i] >= 0.6:
                        escolhas.append('c')
                    else:
                        escolhas.append('d')
        return escolhas