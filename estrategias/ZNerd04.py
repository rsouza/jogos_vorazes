# coding: utf8

mensagens = ['||| ESTOU CANSADO! |||',                     '||| CUIDADO COM OS PASSARINHOS |||',
             '||| PORQUE NÃO COOPERAMOS, AMIGOS? |||',     '||| A RESPOSTA PARA TUDO: 42 |||',
             '||| SE ELEITO, CAÇAREI COMO TODOS |||',      '||| SOU O SR MISICS, OLHE PARA MIM! |||',
             '||| NÃO QUERO MORRER, SR STARK |||',         '||| A SOLUCAO AQUI É TRIVIAL... DESCANSAR |||',
             '||| PAI... TENHO FOME... |||',               '||| DESCANÇA... DESCANÇA... DESCANSA... |||',
             '||| PAI... TENHO SEDE... |||',               '||| PORQUE CAÇAR HOJE? POSSO CAÇAR AMANHA |||',
             '||| EU USO O NECESSARIO |||',                '||| VINGADORES: A RODADA INFINITA |||',
             '||| SOMENTE O NECESSARIO |||',               '||| QUEM É ESSE QUE SÓ CAÇA? HEIN?! |||',
             '||| CAÇA COMIGO, GENTE! |||',                '||| O QUE E ESSE m SORTEADO? |||']

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
        """ Distribuicao aleatoria, mas tendenciosa sob as reputaçoes """
        
        if rodada%100 == 0:
            print('\n' + np.random.choice(mensagens) + '\n')
        
        return [self.pensa_cacar(reputacoes, x, reputacao_atual, m) for x in reputacoes]
    
    def pensa_cacar(self, reputacoes, x, reputacao, m):
        aux = ['c', 'd']
        
        media = sum(reputacoes)/len(reputacoes)
        cacam = media*len(reputacoes)**2
        aux.append('d' if reputacao >= 0.6 else 'c')
        aux.append('d' if x < 0.3 or x > 0.8 or x >= media else 'c')
        aux.append('d' if cacam > m else 'c')
        aux.append('d' if cacam > m else 'c')
        
        return np.random.choice(aux)

    def resultado_da_cacada(self, comida_ganha):
        """ Dá os retornos a cada rodada dos jogadores """
        pass

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        """ A cada rodada, recebemos os resultados  """
        #print('Jogador 4 {}'.format(self.historico[-1]))
        pass
