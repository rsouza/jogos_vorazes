
# coding: utf-8

# In[ ]:


from estrategias.jogadores import Jogador
import numpy as np
import random

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        jogadores = len(reputacoes_dos_jogadores)
        
        if rodada == 1:
            escolha = ['c', 'd']
            escolhas = [ random.choice(escolha) for a in reputacoes_dos_jogadores]
            
        if jogadores < 6:
            escolhas = ['d' for i in reputacoes_dos_jogadores]
        
        else:
            for i in reputacoes_dos_jogadores:
                if i > 0.85 and reputacao_atual > 0.65:
                    escolhas.append('d')
                else:
                        if i < 0.5:
                            escolhas.append('d')
                        else:
                             escolhas.append('c')
        return escolhas

