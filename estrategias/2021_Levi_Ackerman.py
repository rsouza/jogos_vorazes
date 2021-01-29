#Pedro Henrique Monteiro Werneck Tavares
from .jogadores import Jogador
import pickle
from numpy import round
import os.path
import random

listaRep1 = [0.5]

class MeuJogador(Jogador):
      
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        escolhas=[None]*len(reputacoes_dos_jogadores)
        
        'criação'
        global listaRep1
         
        arquivo1 = open('estrategias/ArquivoB.pck', 'wb')
        listaRep1.append(round(reputacao_atual,12))
        pickle.dump(listaRep1, arquivo1)
        arquivo1.close()
        
        
        if rodada <= 2:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        elif comida_atual <= 700:
            escolhas = ['d' for x in reputacoes_dos_jogadores]
        elif reputacao_atual < 0.7:
            escolhas = ['c' if x > 0.8 else 'd' for x in reputacoes_dos_jogadores]
        else:
            escolhas = ['d' if x > 0.9 or x < 0.6 else 'c' for x in reputacoes_dos_jogadores]
            
            
            
        if rodada>10:
            for i in range(len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores.count(reputacoes_dos_jogadores[i])>1:
                    escolhas[i]="d"
        
        
    
        
        
        
        if rodada>5:
            'ajudando eren'

            Existe=os.path.exists('estrategias/ArquivoA.pck')
            if Existe==True:

                    #Busca informação'
                file =  open('estrategias/ArquivoA.pck','rb')
                x = pickle.load(file)
                file.close()  



                for i in range(len(reputacoes_dos_jogadores)):
                    casas_dec=12

                    booleano=True
                    while booleano==True:
                        if round(reputacoes_dos_jogadores[i],casas_dec)!=round(x[-1],casas_dec):
                            casas_dec-=1
                            booleano=True
                        else:
                            booleano=False
                        if casas_dec==1:
                            break

                    if round(reputacoes_dos_jogadores[i],casas_dec)==round(x[-1],casas_dec): 
                        escolhas[i]='c'




            'ajudando barbie'
            Existe1=os.path.exists('estrategias/ArquivoC.pck')
            if Existe1==True:

                    #Busca informação'
                file =  open('estrategias/ArquivoC.pck','rb')
                x = pickle.load(file)
                file.close()  
                    #Joga
                for i in range(len(reputacoes_dos_jogadores)):
                    casas_dec=12

                    booleano=True
                    while booleano==True:
                        if round(reputacoes_dos_jogadores[i],casas_dec)!=round(x[-1],casas_dec):
                            casas_dec-=1
                            booleano=True
                        else:
                            booleano=False
                        if casas_dec==1:
                            break

                    if round(reputacoes_dos_jogadores[i],casas_dec)==round(x[-1],casas_dec): 
                        escolhas[i]='c'
            if Existe==False and Existe1==False:
                if rodada <= 2:
                    escolhas = ['c' for x in reputacoes_dos_jogadores]
                elif comida_atual <= 700:
                    escolhas = ['d' for x in reputacoes_dos_jogadores]
                elif reputacao_atual < 0.7:
                    escolhas = ['c' if x > 0.8 else 'd' for x in reputacoes_dos_jogadores]
                else:
                    escolhas = ['d' if x > 0.9 or x < 0.6 else 'c' for x in reputacoes_dos_jogadores]
                if rodada>10:
                    for i in range(len(reputacoes_dos_jogadores)):
                        if reputacoes_dos_jogadores.count(reputacoes_dos_jogadores[i])>1:
                            escolhas[i]="d"
            'ajudando grisha'

            Existe4=os.path.exists('estrategias/ArquivoD.pck')
            if Existe4==True:

                    #Busca informação'
                file =  open('estrategias/ArquivoD.pck','rb')
                x = pickle.load(file)
                file.close()  



                for i in range(len(reputacoes_dos_jogadores)):
                    casas_dec=12

                    booleano=True
                    while booleano==True:
                        if round(reputacoes_dos_jogadores[i],casas_dec)!=round(x[-1],casas_dec):
                            casas_dec-=1
                            booleano=True
                        else:
                            booleano=False
                        if casas_dec==1:
                            break

                    if round(reputacoes_dos_jogadores[i],casas_dec)==round(x[-1],casas_dec): 
                        escolhas[i]='c'
       # print(escolhas.count("c"),rodada)
    
        if rodada>3:
            for i in range(len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores[i]==reputacao_atual:
                    escolhas[i]="c"
        
        return escolhas
