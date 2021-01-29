from estrategias.jogadores import Jogador
import random

class MeuJogador(Jogador):

    def _init_(self):
        Jogador._init_(self)
        self.total_jogador = 0

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        if rodada <= 2:
            for rep in reputacoes_dos_jogadores:
                r = random.random()
                if r > 0.5:
                    escolhas.append('d')
                else:
                    escolhas.append('c')
                    

        elif rodada > 200:
            for rep in reputacoes_dos_jogadores:
                if abs(rep - reputacao_atual) < 0.1:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        else:
            for rep in reputacoes_dos_jogadores:
                if rep > 0.6:
                    escolhas.append('d')
                else:
                    escolhas.append('c')

        return escolhas
