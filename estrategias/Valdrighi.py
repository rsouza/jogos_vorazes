# coding: utf8
from .jogadores import Jogador
import random

class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada==1:
            self.comida=comida_atual
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        elif len(reputacoes_dos_jogadores)<=6:
            escolhas = ['d' for x in reputacoes_dos_jogadores]      
        else:
            escolhas=[]
            for rep in reputacoes_dos_jogadores:
                if not (0.2<rep<0.8):
                    escolhas.append('d')
                else:
                    escolhas.append('c')
                    #aux=random.random()
                    #if aux>rep:
                        #escolhas.append('d')
                    #else:
                        #escolhas.append('c')
        return escolhas

