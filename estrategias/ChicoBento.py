#Estratégia: João Vinícius Primaki Prado
from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    
    def __init__(self):
        self.caso = 0
        
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        jogadores = len(reputacoes_dos_jogadores)
        comidamin = 500
        if comida_atual < comidamin:
            self.caso = 2
        if comida_atual >= comidamin and self.caso == 2:
            self.caso = 1
        if jogadores <= 3:
            self.caso = 3
            
        if self.caso == 1:
            escolhas = ['c' if np.random.random() < x else 'd' for x in reputacoes_dos_jogadores]
        elif self.caso == 0:
            escolhas = ['c'] * jogadores
            self.caso = 1
        elif self.caso == 2 or self.caso == 3:
            escolhas = ['d'] * jogadores
            
        return escolhas