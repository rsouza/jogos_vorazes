# coding: utf8

from estrategias.jogadores import Jogador
import numpy as np

""" Jogador básico """

class MeuJogador(Jogador):

    def __init__(self):
        self.comida = 0
        self.reputacao = 0
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes):
        """ Método principal que executa a cada rodada. """
        """ Distribuicao baseada nas reputacoes medias na rodada """

        aux = sum(reputacoes)/len(reputacoes)
        return ['c' if np.random.rand() >= aux else 'd' for x in reputacoes]       


    def resultado_da_cacada(self, comida_ganha):
        """ Dá os retornos a cada rodada dos jogadores """
        pass
    
    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        """ A cada fim de rodada, recebemos os resultados  """
        #print('Jogador 1 {}'.format(self.comida_atual))
        pass
