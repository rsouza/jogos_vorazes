#Estratégia: João Vinícius Primaki Prado
from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    def __init__(self):
        self.r = 0
        self.listac = []
        self.derivada = 0
        
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada == 1:
            escolhas = ['c'] * len(reputacoes_dos_jogadores)
            self.listac.append(comida_atual)
        else:
            if comida_atual >= self.listac[-1]:
                if self.derivada < 0:
                    self.derivada = 0
                    self.r = 0
                self.derivada += 1
            else:
                if self.derivada > 0:
                    self.derivada = 0
                    self.r = 0
                self.derivada -= 1
            if self.derivada == -10:
                self.derivada = 0
                self.r -= 0.1
            elif self.derivada == 20:
                self.r += 0.1
                
            self.listac.append(comida_atual)
            escolhas = ['c' if np.random.random() < max(a+self.r,0.1) else 'd' for a in reputacoes_dos_jogadores]
        if len(reputacoes_dos_jogadores) <= 3:
            escolhas = ['d'] * len(reputacoes_dos_jogadores)
            
        return escolhas