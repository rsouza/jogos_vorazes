__author__ = 'Bruno Almeida'

from random import choice
from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    
    def __init__(self):
        self.rodada_par = False
    
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        if rodada == 1:
            escolhas = [ 'c' for x in reputacoes_dos_jogadores]
            self.rodada_par = True
        elif len(reputacoes_dos_jogadores)<3 or rodada >=350:
            escolhas = ['c' if x==reputacao_atual else 'd' for x in reputacoes_dos_jogadores]
        else:
           
            if self.rodada_par:
                escolhas = [ 'd' for x in reputacoes_dos_jogadores]
                self.rodada_par = False
            else:
                escolhas = [ 'c' for x in reputacoes_dos_jogadores]
                self.rodada_par = True
        
        
        
        
        return escolhas
    
