from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):

        media = sum(reputacoes_dos_jogadores) / len(reputacoes_dos_jogadores)
        escolhas = []
        if 5 <= len(reputacoes_dos_jogadores):   
            for rep in reputacoes_dos_jogadores:
                if rep >= media:
                    escolhas.append('d')
                else:
                    escolhas.append('c')
        else:
            for rep in reputacoes_dos_jogadores:
                escolhas.append('d')
        return escolhas
#Renan Ferreira de Moura