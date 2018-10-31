# -*- coding: utf8 -*-
from estrategias.jogadores import Jogador

import numpy as np

class MeuJogador(Jogador):
    
    #Jogador principal. Ele ser utiliza de alguns métodos que serão logo apresentados.

    def __init__(self):
        #define algumas variáveis interessantes
        self._name = "Moschen3"
        self.hist_comida = []
        self.n_inicial_jogadores = 0
        self.hist_m = []
        self.hist_reputacao = []
        self.muda_estrategia = 0
        self.fim = 0
        
    def escolha_de_cacada(self,rodada,comida_atual,reputacao_atual,m,reputacoes_dos_jogadores):
        
        # atualiza variáveis de história 
        self.hist_comida.append(comida_atual)
        self.hist_reputacao.append(reputacao_atual)
        self.hist_m.append(m)
        
        # número de jogadores 
        n_jogadores = len(reputacoes_dos_jogadores)
        
        if rodada == 1:
            self.n_inicial_jogadores = n_jogadores

        #estratégia
       
        if n_jogadores > self.n_inicial_jogadores/4:
            escolhas = self.aleatorio(reputacoes_dos_jogadores,reputacao_atual)
            return escolhas

        elif n_jogadores>=2: 
            escolhas = self.tange(reputacao_atual,n_jogadores)
            escolhas = escolhas*n_jogadores
            return escolhas
               
        elif self.muda_estrategia == 2:
            escolhas = ['d']
            return escolhas
    
    def tange(self,reputacao_atual,n_jogadores):
        if n_jogadores >=7:                               
            if reputacao_atual > 0.45:
                escolha = ['d']
            else:
                escolha = ['c']
        else:
            if reputacao_atual > 0.4:
                escolha = ['d']
            else:
                escolha = ['c']        
        return escolha
    
    def aleatorio(self,reputacoes_dos_jogadores,reputacao_atual):
        media = np.mean(reputacoes_dos_jogadores)
        desvpad = np.std(reputacoes_dos_jogadores)
        alea = np.random.normal(media,desvpad)
        escolhas = []
        for rep in reputacoes_dos_jogadores:
            if rep > alea:
                escolhas.append('c')
            else:
                escolhas.append('d')
        return escolhas
          
    def resultado_da_cacada(self, comida_ganha):
        pass

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        pass
            
    
    
    

        
        