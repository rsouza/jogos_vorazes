from estrategias.jogadores import Jogador
import random

class MeuJogador(Jogador):
    def __init__(self):
        Jogador.__init__(self)
        self.repAnterior = 0
        self.comidaAnterior = 0

    def escolha_de_cacada(self, rodada, comidaAtual, repAtual, m, repJogadores):
        retorno = []
        if rodada == 1:
            for i in range(len(repJogadores)):
                retorno.append('c')
        elif rodada >= 2:
            total = 0
            qtdRepBaixa = 0
            for i in repJogadores:
                total += i
                if i <= 0.3:
                    qtdRepBaixa +=1
            media = total / len(repJogadores)
            melhorRep = repAtual >= self.repAnterior
            melhorComida = comidaAtual >= self.comidaAnterior
            aceitavel = False
            perdaPossivel = qtdRepBaixa * 3 
            if perdaPossivel < comidaAtual and (perdaPossivel * comidaAtual ) / 100 <= 12:
                aceitavel = True
            #definir escolha    
            for i in repJogadores:
                if melhorRep:
                    escolha = 'd'
                else: escolha = 'c'    
                if i <= 0.3:
                    if aceitavel: escolha = 'c'
                    else: escolha = 'd'    
                elif i > 0.3 and i < 0.6:
                    if melhorComida: escolha = 'c'
                    else: escolha = 'd'
                elif i >= 0.6 and i < 0.85:
                    escolha = random.choice('cd')
                else: escolha = 'c'    
                retorno.append(escolha)
        self.repAnterior = repAtual
        self.comidaAnterior = comidaAtual
        return retorno