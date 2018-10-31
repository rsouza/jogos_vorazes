from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    def __init__(self):
        self.comida = 0
        self.reputacao = 0
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        for reputacao in reputacoes_dos_jogadores:
            if reputacao > 0.75:
                escolhas.append('d')
            else :
                escolhas.append(np.random.choice(['c','d']))
        return escolhas
