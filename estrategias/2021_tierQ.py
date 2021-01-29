# coding: utf8
from estrategias.jogadores import Jogador
class MeuJogador(Jogador):
    def __init__(self):
        self.comida = 0
        self.reputacao = 0
        self.historico = {}
        self.historico2 = {}
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        """
        so caca com jogadores com reputação entre:
        media das reputacoes  -------  media entre media das reputacoes e a maxima das reputacoes
        e na primeira rodada ele caca com 35% dos jogadores
        """
        self.rodada = rodada 
        escolhas = []
        if rodada > 1: 
            min_r = sum(reputacoes_dos_jogadores)/len(reputacoes_dos_jogadores)
            max_r = (max(reputacoes_dos_jogadores) + min_r)/2
            for x in reputacoes_dos_jogadores:
                if x >= min_r and x <= max_r:
                    escolhas.append('d')
                else:
                    escolhas.append('c')
                    
        else:
            cac =  int(len(reputacoes_dos_jogadores)*0.35)*['c']
            desc = (reputacoes_dos_jogadores - len(cac))*['d']
            escolhas = cac + desc
            
        return escolhas

    def resultado_da_cacada(self, comida_ganha):
        self.comida_ganha = comida_ganha

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        pass 
