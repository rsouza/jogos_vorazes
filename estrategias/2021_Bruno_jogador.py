from estrategias.jogadores import Jogador
import numpy as np


class MeuJogador(Jogador):
    
    def __init__(self):
        Jogador.__init__(self)
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        reputacao_media = sum(reputacoes_dos_jogadores)/len(reputacoes_dos_jogadores)
        escolhas = []
        if rodada == 1:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        elif rodada < 300:
            for x in reputacoes_dos_jogadores:
                if x < 0.1 or x > 0.9:
                    escolhas.append('d')
                elif x >= reputacao_media:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        else:
            for x in reputacoes_dos_jogadores:
                if x >= reputacao_atual:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        return escolhas