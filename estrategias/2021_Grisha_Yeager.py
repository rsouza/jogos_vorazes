#Diogo David Sánchez Lima
from estrategias.jogadores import Jogador
import numpy
import numpy as np
import os.path
from numpy import round
import pickle
import random

listaRep5=[]

def n_melhores(a1,n):
    'a=lista    n=posições'
    a=list(a1)
    a.sort()
    return a[-n:]

class MeuJogador(Jogador):
    
    def __init__(self):
        Jogador.__init__(self)
    
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        n_jogadores=len(reputacoes_dos_jogadores)
        'criação'
        global listaRep5
         
        arquivo5 = open('estrategias/ArquivoD.pck', 'wb')
        listaRep5.append(round(reputacao_atual,12))
        pickle.dump(listaRep5, arquivo5)
        arquivo5.close()
        'criado'
        
        meta_reputacao=0.6
        meta_rodada=150
      
        if rodada > meta_rodada:
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
                    
                        
        if rodada>12:
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
                        if casas_dec==3:
                            break

                    if round(reputacoes_dos_jogadores[i],casas_dec)==round(x[-1],casas_dec): 
                        escolhas[i]='c'
            'ajudando levi'

            Existe=os.path.exists('estrategias/ArquivoB.pck')
            if Existe==True:

                    #Busca informação'
                file =  open('estrategias/ArquivoB.pck','rb')
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
                        if casas_dec==3:
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



                for i in range(len(reputacoes_dos_jogadores)):
                    casas_dec=12

                    booleano=True
                    while booleano==True:
                        if round(reputacoes_dos_jogadores[i],casas_dec)!=round(x[-1],casas_dec):
                            casas_dec-=3
                            booleano=True
                        else:
                            booleano=False
                        if casas_dec==3:
                            break

                    if round(reputacoes_dos_jogadores[i],casas_dec)==round(x[-1],casas_dec): 
                        escolhas[i]='c'          
                        
        if comida_atual-3*len(reputacoes_dos_jogadores)<100:
            if len(reputacoes_dos_jogadores)<4:
                if rodada%20==0:
                    escolhas=['d']*len(reputacoes_dos_jogadores)
            
            
        if len(reputacoes_dos_jogadores)<5:
            if comida_atual<50:
                if rodada%100==0:
                    print('=================')
                    print('= T A T A K A E =')
                    print('=================')
        return escolhas
        
        
        
        
        