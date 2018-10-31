
# coding: utf-8

# In[4]:


from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    
    def __init__(self):
        
        Jogador.__init__(self)
        self.dispercao = []
        self.njogadores = []

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        media = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
        var_rep = sum((xi - media) ** 2 for xi in reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
        
        self.dispercao.append(var_rep)
        self.njogadores.append(len(reputacoes_dos_jogadores))
        
        disp = self.dispercao
        jogadores = self.njogadores
        
        if rodada == 1:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
            
        else:
            
            if jogadores[rodada-1] == jogadores[rodada-2] and disp[rodada-1] > disp[rodada-2]:
                escolhas = ['d' for x in reputacoes_dos_jogadores]
            
            elif jogadores[rodada-1] == jogadores[rodada-2] and disp[rodada-1] < disp[rodada-2]:
                escolhas = ['c' for x in reputacoes_dos_jogadores]
                
            elif jogadores[rodada-1] != jogadores[rodada-2] and reputacao_atual > media:
                escolhas = ['d' for x in reputacoes_dos_jogadores]
            
            elif jogadores[rodada-1] != jogadores[rodada-2] and reputacao_atual < media:
                escolhas = ['c' for x in reputacoes_dos_jogadores]
                
            else:
                escolhas = ['d' for x in reputacoes_dos_jogadores]

                
        return escolhas

