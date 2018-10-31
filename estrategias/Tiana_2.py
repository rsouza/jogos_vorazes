
# coding: utf-8

# In[4]:


from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        if rodada == 1:
            escolhas = ['c' for n in reputacoes_dos_jogadores]
        else:
            escolhas = ['d' if np.random.rand() < 0.5 else 'c' for i in reputacoes_dos_jogadores]
        return escolhas

