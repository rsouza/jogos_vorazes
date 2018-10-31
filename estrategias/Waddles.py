from estrategias.jogadores import Jogador
import math
import random
class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas=[]
        if rodada==1:
            escolhas.append('c')
        for k in  reputacoes_dos_jogadores:
            w=random.randint(0,1000)
            if rodada<400:
                if rodada%2==0 or rodada%3==0:
                    if w>600:
                        escolhas.append('c')
                    else:
                        escolhas.append('d')
                else:
                    escolhas.append('c')
            else:
                if sum(reputacoes_dos_jogadores)/len(reputacoes_dos_jogadores)<0.5: #media reputação
                    escolhas.append('d')
                else:
                    escolhas.append('c')
            
        return escolhas