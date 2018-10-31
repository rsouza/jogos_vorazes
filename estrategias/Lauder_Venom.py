from estrategias.jogadores import Jogador
import random

class MeuJogador(Jogador):
    """
    Feito por Lauder Leal
    Ajuda apenas os mais compatíveis
    """
    def __init__(self):
        self._name = "Venom"

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        if rodada == 1:
            for i in range(0,len(reputacoes_dos_jogadores)):
                escolhas.append('c')
        elif rodada < 500:
            for i in range(0,len(reputacoes_dos_jogadores)):
                if abs(reputacao_atual-reputacoes_dos_jogadores[i]) < 0.175:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        else:
            for i in range(0,len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores[i] > 0.7:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        return escolhas