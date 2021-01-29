from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    
    def __init__(self):
        Jogador.__init__(self)
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        self.rodada=rodada
        reputacoes_dos_jogadores = sorted(reputacoes_dos_jogadores, reverse = True)
    
        if rodada<4:
            escolhas=['c' for x in reputacoes_dos_jogadores]
            
        if rodada>3:
            escolhas=[]
            if len(reputacoes_dos_jogadores)>m:
                for i in range(len(reputacoes_dos_jogadores)):
                    if reputacoes_dos_jogadores[i] >= 0.6:
                        escolhas.append('c')
                    else:
                        escolhas.append('d')
                    
            elif len(reputacoes_dos_jogadores)<=m:
                for i in range(len(reputacoes_dos_jogadores)):
                    escolhas.append('d')

        return escolhas  
        
