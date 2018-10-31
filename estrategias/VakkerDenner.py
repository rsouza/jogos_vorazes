
from estrategias.jogadores import Jogador
class MeuJogador(Jogador):
   
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        k=0
        r = 0
        if k==0:
            Med_Rep = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
            escolhas = []
            for rep in reputacoes_dos_jogadores:
                if rep >= Med_Rep:
                    escolhas.append('d')
                else:
                    escolhas.append('c')
            for i in range(2000):
                r=r+1
            if r == 2000:
                k = 0
            return escolhas
        else:
            r = 0

            for i in range(2000):
                escolhas = ['c' for x in reputacoes_dos_jogadores]
                r=r+1
            if r == 2000:
                k = 1
            return escolhas

#Rodrigo Zillo