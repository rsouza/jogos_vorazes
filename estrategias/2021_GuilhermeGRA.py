

#Guilherme Gustavo Roca Arenales
'''
Disclaimer:
Este script foi criado após diversas simulações entre os mais de 100 classes de estratégias de jogadores disponibilizados.
Após as sucessivas simulações variando-se o número de rodadas e quantidade de inicial de comida, foram removidos os piores jogadores para deixar aproximadamente
apenas os 40 - 50 melhores colocados nas simulações.
Foram feitas algumas simulações a mais para verificar se com um número menor de jogadores, os primeiros a serem eliminados e os últimos a serem eliminados, seriam
os mesmos. Foi verificado que isso de fato acontece: os vencedores e os perdedores tendem a ser os mesmos independentemente do número de jogadores.
Foi notado que dentre os vencedores existem basicamente três "grupos" que sempre estão bem posicionados:
Grupo Atílio, grupo damn/shit/fuck e grupo Tomas-Coringa.


Assim, após estudar os códigos dos jogadores, foi decidida a impleentação de uma versão modificada do jogador Atilio_XXXXX.

Portanto, este código tem a inteção de bater o desempenho dos jogadores "Atílio", para a maioria das condições iniciais de comida e rodadas.
Por outro lado, esta escolha possui um ponto fraco que são os jogadores damn/shit/fuck, já que estes tendem a colaborar entre si, a partir de um número avançado
de rodadas, criando uma condição de ganha-ganha entrei si, difícil de ser batida pelo presente jogador.


'''


from estrategias.jogadores import Jogador
import numpy as np


class MeuJogador(Jogador):
    
    def __init__(self):
        Jogador.__init__(self)
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        meta_reputacao=0.602
        meta_rodada=205
       
    
        if rodada <= 4:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
            return escolhas
        elif rodada > meta_rodada:
            escolhas=[]
            for i in range(len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores[i] == reputacao_atual:
                    escolhas=escolhas+['c']
                else:
                    escolhas=escolhas+['d']
            return escolhas  
        
        else:
            escolhas=[]
            for i in range(len(reputacoes_dos_jogadores)):
                    if (rodada != 1) and (reputacoes_dos_jogadores[i]==1 or reputacoes_dos_jogadores[i]==0):
                        escolhas=escolhas+['d']
                    elif reputacao_atual > meta_reputacao:
                        escolhas=escolhas+['d']
                    else:
                        escolhas=escolhas+['c']
            return escolhas