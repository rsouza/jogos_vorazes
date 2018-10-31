from estrategias.jogadores import Jogador
import random
listinha = [1, 42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672, 714, 756, 798, 840, 882, 924, 966, 1008, 1050, 1092, 1134, 1176, 1218, 1260, 1302, 1344, 1386, 1428, 1470, 1512, 1554, 1596, 1638, 1680, 1722, 1764, 1806, 1848, 1890, 1932, 1974, 2016]
class MeuJogador(Jogador):

    def __init__(self):
        Jogador.__init__(self)
        self.total_jogador = 0

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada in listinha:
            self.total_jogador = len(reputacoes_dos_jogadores)

        escolhas = []
        n_jogadores =  len(reputacoes_dos_jogadores)
        media = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
        for rep in reputacoes_dos_jogadores:
            if (rep >= 0.42) and random.uniform(0, 1) > (1.1 - n_jogadores / self.total_jogador):
                escolhas.append('d')
            else:
                escolhas.append('c')
        return escolhas
#Renan Ferreira de Moura