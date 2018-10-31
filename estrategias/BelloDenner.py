# coding: utf8
from .jogadores import Jogador
import numpy.random as npr
import os
listamagica = [42, 84, 126, 168, 210, 252, 294, 336, 378, 420, 462, 504, 546, 588, 630, 672, 714, 756, 798, 840, 882, 924, 966, 1008, 1050, 1092, 1134, 1176, 1218, 1260, 1302, 1344, 1386, 1428, 1470, 1512, 1554, 1596, 1638, 1680, 1722, 1764, 1806, 1848, 1890, 1932, 1974, 2016]

class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        if rodada in listamagica:
            escolhas = ['c' for x in reputacoes_dos_jogadores]           
        else:
            npr.seed(seed=int.from_bytes(os.urandom(4), byteorder='big'))
            escolhas = []
            for rep in reputacoes_dos_jogadores:
                esc = npr.choice(['d', 'c'], 1, p=[1 - rep, rep])
                escolhas.append(esc)

        return escolhas
#Renan Ferreira de Moura