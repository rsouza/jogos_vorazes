from estrategias.jogadores import Jogador


class MeuJogador(Jogador):
    '''A ideia é manter a reputação alta para que cassem comigo, porém,
respeitando um limite e não sendo o maior de todos. Além disso, ela cai com o tempo
e no final(quando os que caçam muito morrem) eu passo só a descanças
Consegui ficar em segundo lugar jogando com os jogadores disponíveis quando
fiz o programa'''
    def __init__(self):
        Jogador.__init__(self)


    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        indice_confiavel = 0.75 # definir números empiricamente
        reputacoes_dos_jogadores = list(reputacoes_dos_jogadores)
        confiavel = min(indice_confiavel, max(reputacoes_dos_jogadores))
        numero_de_cacadas = int(confiavel*(len(reputacoes_dos_jogadores)))
        reputacoes_dos_jogadores_sorted = reputacoes_dos_jogadores.copy()
        reputacoes_dos_jogadores_sorted.sort()
        cacadas = reputacoes_dos_jogadores_sorted[0:numero_de_cacadas]
        cont = 0
        escolhas = []
        
        for i in reputacoes_dos_jogadores:
            if i in cacadas and cont != numero_de_cacadas:
                escolhas += 'c'
                cont += 1
            else:
                escolhas += 'd'

        
        #print(comida_atual)
        if len(reputacoes_dos_jogadores) <= 3 or rodada > 280: # definir números empiricamente
            return ['d']*len(reputacoes_dos_jogadores)
        
        return escolhas
