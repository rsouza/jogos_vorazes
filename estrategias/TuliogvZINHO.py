# coding: utf8
from .jogadores import Jogador

class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        if rodada <= 4:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        else:
            escolhas = ['d' for x in reputacoes_dos_jogadores]                            
                   
        return escolhas
