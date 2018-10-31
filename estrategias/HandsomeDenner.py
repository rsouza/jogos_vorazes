from estrategias.jogadores import Jogador
import random
#Danillo Fiorenza
class MeuJogador(Jogador):
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas=[]
        total=len(reputacoes_dos_jogadores)
        if rodada == 1:
            escolhas = ['c' for t in reputacoes_dos_jogadores]
        elif total>10:
            for x in reputacoes_dos_jogadores:
                if random.uniform(0, 1)>reputacao_atual/(x+reputacao_atual):
                    escolhas.append('c')
                else:
                    escolhas.append('d')
        else:
            if comida_atual<2*total:
                escolhas = ['d' for m in reputacoes_dos_jogadores]
            else:
                if random.uniform(0, 1)<k/(k+reputacao_atual):
                    escolhas.append('d')
                else:
                    escolhas.append('c')
        return escolhas
 
                    
                  
                
                