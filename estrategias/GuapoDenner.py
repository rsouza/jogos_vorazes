from .jogadores import Jogador

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        Med_Rep = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
        if reputacao_atual > Med_Rep:
            
            escolhas = ['d' for x in reputacoes_dos_jogadores]
        else:
            escolhas = ['c' for i in reputacoes_dos_jogadores]

        return escolhas

#Rodrigo Zillo