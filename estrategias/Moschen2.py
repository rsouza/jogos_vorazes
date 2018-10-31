# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador

import numpy as np

class MeuJogador(Jogador):
    
    #Jogador principal. Ele ser utiliza de alguns métodos que serão logo apresentados.

    def __init__(self):
        #define algumas variáveis interessantes
        self._name = "Moschen2"
        self.hist_comida = []
        self.n_inicial_jogadores = 0
        self.hist_m = []
        self.hist_reputacao = []
        self.hist_media = []
        self.hist_desvpad = []
        self.muda_estrategia = 0
        
    def escolha_de_cacada(self,rodada,comida_atual,reputacao_atual,m,reputacoes_dos_jogadores):
        
        # atualiza variáveis de história 
        self.hist_comida.append(comida_atual)
        self.hist_reputacao.append(reputacao_atual)
        self.hist_m.append(m)
        self.hist_media.append(np.mean(reputacoes_dos_jogadores))
        self.hist_desvpad.append(np.std(reputacoes_dos_jogadores))
        
        # número de jogadores 
        n_jogadores = len(reputacoes_dos_jogadores)
        if rodada == 1:
            self.n_inicial_jogadores = n_jogadores
            
        if len(self.hist_comida) > 50:  
            if (self.hist_comida[-1]-self.hist_comida[-50]) < -self.hist_comida[-50]/50:
                if self.muda_estrategia == 0:
                    self.muda_estrategia = 1
                else:
                    self.muda_estrategia = 0
        #estratégia
        
        if self.muda_estrategia == 0:

            if n_jogadores > self.n_inicial_jogadores/4:
                escolhas = self.intercala(rodada)
                escolhas = escolhas*n_jogadores
                return escolhas 
            else: 
                escolhas = self.tange(reputacao_atual)
                escolhas = escolhas*n_jogadores
                return escolhas
        
        if self.muda_estrategia == 1:
            
            escolhas = self.aleatorio(reputacoes_dos_jogadores,n_jogadores)
            return escolhas

    def intercala(self,rodada):
        if rodada%7 == 1 or rodada%7 == 3 or rodada%7 == 5 or rodada%7 == 0:
            escolha = ['c']
        else:
            escolha = ['d']
        return escolha
    
    def tange(self,reputacao_atual):
        if reputacao_atual > 0.45:
            escolha = ['d']
        else:
            escolha = ['c']
        return escolha
    
    def aleatorio(self,reputacoes_dos_jogadores,n_jogadores):
        escolhas = []
        for rep in reputacoes_dos_jogadores:
            if (rep >= 0.4) and np.random.uniform() > (1.1 - n_jogadores / self.n_inicial_jogadores):
                escolhas.append('c')
            else:
                escolhas.append('d')
        return escolhas
        
    def resultado_da_cacada(self, comida_ganha):
        pass

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        pass
        
        