from estrategias.jogadores import Jogador
from statistics import median
from random import choice

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        media = sum(reputacoes_dos_jogadores)/len(reputacoes_dos_jogadores)
        vivos = len(reputacoes_dos_jogadores)
        mediana = median(reputacoes_dos_jogadores)

        if rodada < 100:
            escolhas = [choice(['d','c']) for x in reputacoes_dos_jogadores]

        elif m <= vivos or comida_atual > 1500 or mediana > 0.49:
            escolhas = ['d' for x in reputacoes_dos_jogadores]

        elif (comida_atual > 1000 and comida_atual < 1499) and media < 0.49:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
            
        return escolhas