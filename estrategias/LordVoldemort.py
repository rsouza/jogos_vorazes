__author__ = 'TLAndrade'

from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    # Avada kedavra.
    def __init__(self):
        self.qtd_jogos = 0
        self.caca_Bela = 0
        self.rep_Bela = 0
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        qtd_jogadores = len(reputacoes_dos_jogadores)
        esc_Bela = ['d' if rodada%5 == 0 else 'c' for x in reputacoes_dos_jogadores]      
        
        # primeiras rodadas jogadores não apresentam estratégia.
        if rodada < 3:
            escolhas = list(np.random.choice(['c','d'], size=qtd_jogadores, p=(0.58,0.42)))
            
        elif rodada%31 == 0:
            escolhas = ['d' for x in range(qtd_jogadores)]
            
        else:
            if rodada>50 and comida_atual < 1200:
                escolhas = ['d' for x in range(qtd_jogadores)]
            else: 
                
                escolhas = []
                if reputacao_atual > 0.58 : ## 0.6
                    for x in reputacoes_dos_jogadores:
                        if x > (self.rep_Bela-0.0003) and x < (self.rep_Bela+0.0003):
                            if rodada%5 == 0:
                                escolhas.append('d')
                            else:
                                escolhas.append('c')
                        elif x == 1:
                            escolhas.append('c')
                        elif x > 0.6:
                            escolhas.append('d')
                        else:
                            escolhas.append('c')
                                       
                elif reputacao_atual > 0.5 :
                    for x in reputacoes_dos_jogadores:
                        if x > (self.rep_Bela-0.0003) and x < (self.rep_Bela+0.0003):
                            if rodada%5 == 0:
                                escolhas.append('d')
                            else:
                                escolhas.append('c')
                        elif x ==1:
                            escolhas.append('d')
                        elif x < 0.55:
                            escolhas.append('d')
                        else:
                            escolhas.append('c')
                else:
                    for x in reputacoes_dos_jogadores:
                        if x > (self.rep_Bela-0.0003) and x < (self.rep_Bela+0.0003):
                            if rodada%5 == 0:
                                escolhas.append('d')
                            else:
                                escolhas.append('c')
                        elif x ==1:
                            escolhas.append('d')
                        elif x < 0.45: ###
                            escolhas.append('d')
                        else:
                            escolhas.append('c')
                                            
                                            
        self.qtd_jogos = self.qtd_jogos + len(reputacoes_dos_jogadores)
        self.caca_Bela = self.caca_Bela + esc_Bela.count('c')
        self.rep_Bela = self.caca_Bela / self.qtd_jogos
              
        return escolhas
                
                      
                   
        
        