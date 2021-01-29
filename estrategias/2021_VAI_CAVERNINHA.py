from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacao_dos_jogadores):
        
        meta_rodada = 200
        meta_reputação = 0.4
        
        if rodada > meta_rodada:
            escolhas = ['d' if rodada != 1 and reputacao_dos_jogadores[i] == 1 or reputacao_dos_jogadores[i] == 0 and reputacao_atual > meta_reputacao else 'c' for i, j in enumerate(reputacao_dos_jogadores)]
        else:
            escolhas = ['c' if reputacao_dos_jogadores[i] == reputacao_atual else 'd' for i, j in enumerate(reputacao_dos_jogadores)]
        
        return escolhas
