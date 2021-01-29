# coding: utf8


import numpy as np
import ipdb
from estrategias.jogadores import Jogador
from collections import defaultdict


"""
 Jogador básico
 O seu Jogador deve ser implementado como uma subclasse de Jogador,
 porem com o seu nome (p.ex. JoseSilva) como nome a classe. A subclasse deve 
 reimplementar os métodos escolha_de_cacada, resultado_da_cacada e 
"""

#hunt_ambos - hunt_solo - descansou_ambos - descansou_solo
score_cacada = [0,-3,-2,1]


class MeuJogador(Jogador):

    def __init__(self):
        """
        Este metodo é executado quando o seu jogador for instanciado no início do jogo.
        
        Você pode adicionar outras variáveis a seu critério.
        
        Você não precisa definir comida ou reputação pois o Controlador do jogo vai manter o registro
        destas variáveis para cada jogador informando-as aos jogadores a cada rodada, através do método
        escolha_de_cacada.

        
        """

        self.comida_inicial = 0
        self.comida = []
        self.reputacao_minha = []
        self.reputacao_jogs = []
        self.historico_jogs = dict()
        self.historico_food_jogs = dict()
        self.prob_c = 0.3
        self.prob_d = 0.7
        self.choices = ['c','d']
        self.jogs_ativos = 0
        
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        """
        Método principal que executa a cada rodada.
        você precisa criar uma lista de escolhas onde 'c' significa escolher caçar e 'd' representa descansar
        as decisãoes podem usar todas as informações disponíveis, por exemplo, as reputações dos outros jogadores.
        rodada: inteiro que é a rodada em que você está
        comida_atual: inteiro com a comida que você tem
        reputacao_atual: float representando sua reputação atual
        m: inteiro que é um limiarde cooperação/caçada desta rodada.
        reputacoes_dos_jogadores: lista de floats com as reputações dos outros jogadores
        """
        #Inicia algumas variáveis de start
        if rodada == 1:
            self.comida_inicial = comida_atual

        self.comida.append(comida_atual)
        self.reputacao_minha.append(reputacao_atual)
        self.reputacao_jogs.append(reputacoes_dos_jogadores)
        
        self.jogs_ativos = len(reputacoes_dos_jogadores)

        #print(rodada)
        #print(comida_atual)
        #print(reputacao_atual)
        #print(m)
        if rodada >= 5:
            best_jogs_list = []
            rate_cacada_list = []
            jogs = list(self.historico_food_jogs.keys())
            food = list(self.historico_food_jogs.values())

            #Top jogadores
            if self.jogs_ativos >= 100:
                jogs_top = 15
            elif self.jogs_ativos >= 50:
                jogs_top = 10
            elif self.jogs_ativos >=10:
                jogs_top = 5
            else:
                jogs_top = 1

            for i in range(0,jogs_top):
                better_food = max(food)
                better_food_idx = food.index(better_food)
                

                best_jogs_list.append(jogs[better_food_idx])

                #Ultimas 3 rodadas dos melhores jogadores
                cacadas_best_jog = self.historico_jogs[jogs[better_food_idx]][-3:]
                
                for cacada in cacadas_best_jog:
                    rate_cacada_list.append((cacada[0] + cacada[1]) / sum(cacada))

                jogs.pop(better_food_idx)
                food.pop(better_food_idx)

            avg_rate_cacada = sum(rate_cacada_list) / len(rate_cacada_list)

            self.prob_c = round(avg_rate_cacada,2)
            self.prob_d = 1-self.prob_c

            #ipdb.set_trace()
            escolhas = [np.random.choice(self.choices,size=1,p=[self.prob_c,self.prob_d])[0] for x in reputacoes_dos_jogadores]
        else:   
            #Escolhas aleatórias até rodada 50
            escolhas = [np.random.choice(self.choices,size=1,p=[self.prob_c,self.prob_d])[0] for x in reputacoes_dos_jogadores]
       

        if rodada % 50:
            #print(self.historico_food_jogs)
            pass

        return escolhas
    
    


    def resultado_da_cacada(self, comida_ganha):
        """
        este método é chamado depois que todas as cacadas da rodada forem terminadas.
        comida_ganha é uma lista com inteiros representando a comida ganha em cada uma das caçadas feitas na rodada. 
        Estes números podem ser negativos.
        
        Sua comida total é a soma destes números e a comida atual.
        
        adicione código para atualizar suas variáveis internas 
        
        """

        for i in comida_ganha:
            if isinstance(i,str):
                
                value = comida_ganha[i]
                
                if i in self.historico_jogs.keys():
                    #Comida por jogador
                    self.historico_food_jogs[i] = self.historico_food_jogs[i] + sum(value)
                    #Historico de performance
                    self.historico_jogs[i].append([value.count(score_cacada[0]),
                                                    value.count(score_cacada[1]),
                                                    value.count(score_cacada[2]),
                                                    value.count(score_cacada[3])])
                else:
                    #Comida por jogador
                    self.historico_food_jogs[i] = self.comida_inicial + sum(value)
                    #Historico de performance
                    self.historico_jogs[i] = list()
                    self.historico_jogs[i].append([value.count(score_cacada[0]),value.count(score_cacada[1]),
                                                                value.count(score_cacada[2]),value.count(score_cacada[3])])


        #print(self.historico_food_jogs)
        pass

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        """
        Adicione código para alterar suas variaveis com base na cooperação que ocorreu na última rodada 
        recompensa: Comida total que você recebeu de jogadores que cooperaram na ultima rodada.
        numero_de_cacadores: inteiro que é o numero de caçadores que cooperou com você na última rodada.
        

        for key,value in recompensa.items():
            if key in self.historico_jogs.keys():
                self.historico_jogs[key].append([value.count(score_cacada[0]),
                                                 value.count(score_cacada[1]),
                                                 value.count(score_cacada[2]),
                                                 value.count(score_cacada[3])])
            else:
                self.historico_jogs[key] = list(value.count(score_cacada[0]),value.count(score_cacada[1]),
                                                value.count(score_cacada[2]),value.count(score_cacada[3]))

        """
        #print("Recompensa: {}".format(recompensa)) 
        #print(m)
        #print(numero_de_cacadores)
        #print(self.historico_jogs)
        if recompensa > 0:
            for key in self.historico_food_jogs:
                self.historico_food_jogs[key]+=recompensa

        

        pass
