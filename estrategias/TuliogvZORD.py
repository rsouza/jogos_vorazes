# coding: utf8
from .jogadores import Jogador

class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        escolhas = []
        
        if rodada <= 5:
            
            escolhas = ['c' for x in reputacoes_dos_jogadores]
            
        else:
            
            for i in reputacoes_dos_jogadores:
            
                media_reputacoes = sum(reputacoes_dos_jogadores)/len(reputacoes_dos_jogadores)
            
                if i < media_reputacoes:
                
                    escolhas.append('c')
                
                else:
                
                    escolhas.append('d')
                    
        return escolhas
