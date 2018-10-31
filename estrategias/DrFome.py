# coding: utf8
from .jogadores import Jogador

class MeuJogador(Jogador):  
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada==1:
            self.comida=comida_atual
            escolhas=['c' for x in reputacoes_dos_jogadores]
        elif comida_atual>5*self.comida:
            escolhas=['d' for x in reputacoes_dos_jogadores]
        else:
            escolhas=[]
            for x in reputacoes_dos_jogadores:
                if 0.4<x<0.8:
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        return escolhas
            