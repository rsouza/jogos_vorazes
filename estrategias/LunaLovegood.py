__author__ = 'TLAndrade'


from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        qtd_jogadores = len(reputacoes_dos_jogadores)
        
        # primeiras rodadas jogadores não apresentam estratégia.
        if rodada < 3:
            escolhas = list(np.random.choice(['c','d'], size=qtd_jogadores, p=(0.58,0.42)))        
        
        else:
            
            if qtd_jogadores < 10:
                    escolhas = ['d' for x in range(qtd_jogadores)]
            else:
                if rodada>50 and comida_atual < 1200:
                    escolhas = ['d' for x in range(qtd_jogadores)]
                
                else: 
                
                    escolhas = []
                    if reputacao_atual > 0.58 : ## 0.6
                        for x in reputacoes_dos_jogadores:
                            if x > 0.6:
                                escolhas.append('d')
                            else:
                                escolhas.append('c')
                                           
                    elif reputacao_atual > 0.5 :
                        for x in reputacoes_dos_jogadores:
                            if x < 0.55:
                                escolhas.append('d')
                            else:
                                escolhas.append('c')
                    else:
                        for x in reputacoes_dos_jogadores:
                            if x < 0.45:
                                escolhas.append('d')
                            else:
                                escolhas.append('c')
                        
       # if rodada%20 == 0:
            #print(comida_atual)
            #print(reputacao_atual)
                                
                        
            
                
                        
        #if rodada%20 == 0:
          #  print("TTTT")
        
        return escolhas
                
                        
                   