from estrategias.jogadores import Jogador
import random

class MeuJogador(Jogador):

    def __init__(self):
        Jogador.__init__(self)
        self.total_jogador = 0

    def escolher_cacar_ou_descansar(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada == 1:
            self.total_jogador = len(reputacoes_dos_jogadores)

        escolhas = []
        n_jogadores_vivos =  len(reputacoes_dos_jogadores)
        media = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
        for rep in reputacoes_dos_jogadores:
            if (rep >= 0.50) and random.uniform(0, 1) > (1.2 - n_jogadores_vivos / self.total_jogador):
                escolhas.append('c')
            else:
                escolhas.append('d')
        return escolhas
