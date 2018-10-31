from estrategias.jogadores import Jogador
import numpy as np

class MeuJogador(Jogador):
    def __init__(self):
        self.comida = 0
        self.reputacao = 0
        self.medias_rep = []
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas = []
        self.medias_rep.append(np.mean(reputacoes_dos_jogadores))
        if rodada <= 20:
            for reputacao in reputacoes_dos_jogadores:
                if reputacao > 0.75:
                    escolhas.append('d')
                else :
                    escolhas.append(np.random.choice(['c','d']))
        else:
            if comida_atual < 25: #se ficar crítico
                for reputacao in reputacoes_dos_jogadores:
                    escolhas.append('d')
            else:
                var_medias = [] #da a variação das últimas 5 médias de reputações; se tiver caindo, descansa mais que caça.
                for i in range(-20,-1):
                    var_medias.append(self.medias_rep[i+1] - self.medias_rep[i])
                if all([i<0 for i in var_medias]) or all([i>0 for i in var_medias]):
                    for rep in reputacoes_dos_jogadores:
                        if reputacao > 0.75: #se o cara for brabo
                            escolhas.append('d')
                        else: #se não, vai no chute
                            chute = np.random.rand()
                            if chute > 0.75:
                                escolhas.append('c')
                            else:
                                escolhas.append('d')
                else: #se não tem tend clara
                    for reputacao in reputacoes_dos_jogadores:
                        if reputacao > 0.75: #se o cara for brabo
                            escolhas.append('d')
                        else: #se não, random.
                            escolhas.append(np.random.choice(['c','d']))
                
        return escolhas
