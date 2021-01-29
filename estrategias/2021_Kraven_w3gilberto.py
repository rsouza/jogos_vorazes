
##ESTRATEGIA JOGADOR - KRAVEN O CACADOR - GILBERTO RAMOS

#IMPORTA JOGADOR DO PACOTE ESTRATEGIAS
from estrategias.jogadores import Jogador
from collections import defaultdict
import numpy as np
import pandas as pd
nameschars = ["Cascao", "ChicoBento", "Kraven_w3gilberto"]
namechar = nameschars[2]
alt = len(nameschars) - 1
##DEFINE PERCENTUAL DE ESCOLHAS
perc = 0.5
#---------------------
medi = lambda x: (np.sqrt(400) - np.sqrt(x))/100

##DEFINE CLASSE MEU JOGADOR
class MeuJogador(Jogador):
    def aprox(self, n):
        saida = [(a,abs(self.historico[a]['reputacao']-n)) for a in self.jogadores]
        a = min(saida, key=lambda x: x[1])[0]
        self.jogadores.remove(a)
        return a

##INICIALIZA CLASSE/CONSTRUTOR    
    def __init__(self):
        self.historico = defaultdict(lambda: {"comida": 0, "reputacao": 0, "cacou": 0, "descansou": 0, "var":0})
        self.self = {"cacou": 0, "descansou": 0, "ult":0}
        self.jogadores = None 

##ESCOLHE MODO CAÇADA        
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada > 1:
            if isinstance(reputacao_atual, np.ndarray):
                reputacao_atual = reputacao_atual[0]
            escolhas = [None]*len(reputacoes_dos_jogadores)
            
            o = sum([self.historico[i]["reputacao"] for i in nameschars[1:]])
            c, d, t= self.self['cacou'], self.self['descansou'], len(reputacoes_dos_jogadores) - alt
            m = (sum(reputacoes_dos_jogadores)-o)/t + medi(rodada) if t > 0 else 0
            b = (1-m)*t - (d+c)*m + c
            b = b//1 + 1 if b > 0 else 1

            maxcomida = sorted([self.historico[i]["comida"] for i in self.jogadores], reverse=True)[:int(b+alt)]
            
            for k,i in enumerate(reputacoes_dos_jogadores):
                if isinstance(i, np.ndarray):
                    i = i[0]
                quem = self.aprox(i)
                
                if quem in nameschars:
                    escolhas[k] = 'c'
                elif self.historico[quem]["comida"] in maxcomida:
                    escolhas[k] = 'd'
                else:
                    escolhas[k] = 'c'
                    
        else:
            escolhas = list(np.random.choice(['d', 'c'], size=len(reputacoes_dos_jogadores), p=(1-perc, perc)))
            self.self["ult"] = escolhas.count('d')/len(escolhas)
        return escolhas

## METODO RESULTADO DA CAÇADA    
    def resultado_da_cacada(self, comida_ganha):
        escolhas = pd.DataFrame(comida_ganha)
        self.jogadores = list(escolhas.columns)
        if namechar in self.jogadores:
            self.self["cacou"] += sum([e == -3 or e == 0 for e in escolhas[namechar]])
            self.self["descansou"] += sum([e == -2 or e == 1 for e in escolhas[namechar]])
            self.jogadores.remove(namechar)
        for nome in self.jogadores:
            self.historico[nome]["cacou"] += sum([e == -3 or e == 0 for e in escolhas[nome]])
            self.historico[nome]["descansou"] += sum([e == -2 or e == 1 for e in escolhas[nome]])
            self.historico[nome]["comida"] += sum(escolhas[nome])
            var = self.historico[nome]["cacou"] / (float(self.historico[nome]["cacou"] + self.historico[nome]["descansou"]))
            self.historico[nome]["var"] =  self.historico[nome]["reputacao"] - var
            self.historico[nome]["reputacao"] = var