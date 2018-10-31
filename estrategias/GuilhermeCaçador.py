from estrategias.jogadores import Jogador
import random

class MeuJogador(Jogador):

    def __init__(self):
        Jogador.__init__(self)
        self.total_jogador = 0

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        escolhas = []
        
        for rep in reputacoes_dos_jogadores:
            if int(rep)<reputacao_atual:
                escolhas.append('d')
            else:
                escolhas.append('c')
            
        return escolhas