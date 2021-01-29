from estrategias.jogadores import Jogador
import pickle
from numpy import round
import os.path
import random

listaRep2=[]

class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        
        'criação'
        global listaRep2
         
        arquivo2 = open('estrategias/ArquivoC.pck', 'wb')
        listaRep2.append(round(reputacao_atual,12))
        pickle.dump(listaRep2, arquivo2)
        arquivo2.close()
        
        
        escolhas = []
        a = []
        b = []
        x = 0
        rj = sorted(reputacoes_dos_jogadores, reverse=True)
        comida = 0
        if rodada == 1:
            comida = comida_atual
        if rodada < 2:
            escolhas = ['c' for x in reputacoes_dos_jogadores]
        else:
            for i in reputacoes_dos_jogadores:
                x += i
            med = x/len(reputacoes_dos_jogadores)
            for i in rj:
                if i < reputacao_atual:
                    a.append('d')
                else:
                    a.append('c')
                if i < med:
                    b.append('d')
                else:
                    b.append('c')
            if a.count('d') < b.count('d'):
                escolhas = a
            else:
                escolhas = b
                
        if rodada>10:
            for i in range(len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores.count(reputacoes_dos_jogadores[i])>1:
                    escolhas[i]="d"
                    
                    
        if rodada>4:
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


            'ajudando levi'

            Existe1=os.path.exists('estrategias/ArquivoB.pck')
            if Existe1==True:

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
                        if casas_dec==1:
                            break

                    if round(reputacoes_dos_jogadores[i],casas_dec)==round(x[-1],casas_dec): 
                        escolhas[i]='c'
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
                    
        if rodada>3:
            for i in range(len(reputacoes_dos_jogadores)):
                if reputacoes_dos_jogadores[i]==reputacao_atual:
                    escolhas[i]="c"
            
            
            
        return escolhas