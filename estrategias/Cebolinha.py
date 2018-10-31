#Estratégia: João Vinícius Primaki Prado
from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    
    def __init__(self):
        self.caso = 0
        
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        jogadores = len(reputacoes_dos_jogadores)
        comidamin = 200
        comidamed = 1000
        if rodada > 100:
            if comida_atual < comidamed and comida_atual >= comidamin:
                self.caso = 2
            if comida_atual < comidamin:
                self.caso = 3
            if comida_atual >= comidamed and self.caso == 2:
                self.caso = 1
            if comida_atual >= comidamin and self.caso == 3:
                self.caso = 2
            if jogadores <= 3:
                self.caso = 4
            
        if self.caso == 1:
            escolhas = ['c' if np.random.random() < a else 'd' for a in reputacoes_dos_jogadores]
        elif self.caso == 0:
            escolhas = ['c'] * jogadores
            self.caso = 1
        elif self.caso == 2:
            #escolhas = ['d' for a in reputacoes_dos_jogadores]
            escolhas = ['c' if np.random.random() < a/2 else 'd' for a in reputacoes_dos_jogadores]
        elif self.caso == 3:
            escolhas = ['c' if np.random.random() < a/3 else 'd' for a in reputacoes_dos_jogadores]
            #escolhas = ['c' if np.random.random() > 0.6 else 'd' for a in reputacoes_dos_jogadores]
        elif self.caso == 4:
            escolhas = ['d'] * jogadores
            
        return escolhas