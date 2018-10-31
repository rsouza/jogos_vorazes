#Atílio Leitão Pellegrino
from estrategias.jogadores import Jogador
import numpy as np


class MeuJogador(Jogador):
    
    def __init__(self):
        Jogador.__init__(self)
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        meta_reputacao=0.602
        meta_rodada=200
      
        if rodada > meta_rodada:
            escolhas=[]
            for i in range(len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores[i] == reputacao_atual:
                    escolhas=escolhas+['c']
                else:
                    escolhas=escolhas+['d']
            return escolhas  
        
        else:
            escolhas=[]
            for i in range(len(reputacoes_dos_jogadores)):
                    if (rodada != 1) and (reputacoes_dos_jogadores[i]==1 or reputacoes_dos_jogadores[i]==0):
                        escolhas=escolhas+['d']
                    elif reputacao_atual > meta_reputacao:
                        escolhas=escolhas+['d']
                    else:
                        escolhas=escolhas+['c']
            return escolhas