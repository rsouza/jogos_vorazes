from estrategias.jogadores import Jogador
import random 
class MeuJogador(Jogador):
    def __init__(self):
        Jogador.__init__(self)
            
    def escolha_cacada(self,rodada,comida_atual,reputacao_atual,m,reputacoes_dos_jogadores):
        quant_dos_jogadores=len(reputacoes_dos_jogadores)
        escolha=[]
        if rodada==1:
            escolha=[random.choice('c','d')for x in reputacoes_dos_jogadores]
        elif 1<rodada<=4:
            escolha=['c'for x in reputacoes_dos_jogadores]
        else:
            for x in reputacoes_dos_jogadores:
                if x > 0.85 and reputacao_atual > 0.55:
                    escolha.append('c')
                else:
                    if 0.5< x <0.8:
                        escolha.append('c')
                    else:
                        escolha.append('d')
            
      
            
        return escolha
