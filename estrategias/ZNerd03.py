# coding: utf8

from estrategias.jogadores import Jogador
import numpy as np

""" Jogador básico """

class MeuJogador(Jogador):

    def __init__(self):
        self.comida = 0
        self.reputacao = 0
        
        self.estrategia = True
        self.historico = []
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes):
        """ Método principal que executa a cada rodada. """
        """ Distribuicao aleatoria baseada nas reputacoes medias na rodada """
        self.historico.append(comida_atual)
        if rodada == 1: self.historico *= 3


        razao_caca = sum(reputacoes)/len(reputacoes)
        return [self.pensa_cacar(reputacoes, razao_caca, reputacao_atual) for x in reputacoes]       

    def pensa_cacar(self, reputacoes, razao, reputacao):
        """ funcao interna, de decisao de cacada """
        """ analisa a variacao da curva de comida recente """
        
        if self.historico[-3] - self.historico[-2] > self.historico[-2] - self.historico[-1]:
            self.estrategia = not self.estrategia
        
        return 'c' if (np.random.rand() >= razao) == self.estrategia else 'd'

    def resultado_da_cacada(self, comida_ganha):
        """ Dá os retornos a cada rodada dos jogadores """
        pass

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        """ A cada rodada, recebemos os resultados  """
        #print('Jogador 3 {}'.format(self.historico[-1]))
        pass
