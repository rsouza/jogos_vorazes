__author__ = 'TLAndrade'


from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        escolhas = [ 'd' if rodada%5 == 0 else 'c' for x in reputacoes_dos_jogadores]
                
        return escolhas
        
        ### Mantem sua reputação constante para ser identificada por Voldemord, e caça para que ele descanse.
    #    intercala = 0
    #    q = len(reputacoes_dos_jogadores)
    #    if rodada%2 == 1:
    #        escolhas = ['c' for x in range(q)]
    #    elif rodada%2 == 0:
    #        escolhas = ['d' for x in range(q)]
    #        
    #        if rodada%20 ==0:
    #            print(reputacao_atual)
    #    return escolhas
        
        
     #   if q%2 == 1 and intercala == 0:
     #       escolhas =  ['d' for x in range(int(np.floor(q/2))+1)] + ['c' for x in range(int(np.floor(q/2)))]
     #       intercala = 1
     #   elif q%2 == 1 and intercala == 1:
     #       escolhas =  ['d' for x in range(int(np.floor(q/2)))] + ['c' for x in range(int(np.floor(q/2))+1)]
     #       intercala = 0
     #   else:    
     #       escolhas =  ['d' for x in range(int(q/2))] + ['c' for x in range(int(q/2))]
            
            
     #   np.random.shuffle(escolhas)
    
        
        
        
                                
                        
            
                
                        
       
                
                        
                   