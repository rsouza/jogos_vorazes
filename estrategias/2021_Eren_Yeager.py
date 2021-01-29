#Alan Gustavo Weiler Gayger

from estrategias.jogadores import Jogador
import os.path
import numpy
from numpy import round
import pickle
import random

listaRep = [0.5]

def n_melhores(a1,n):
    'a=lista    n=posições'
    a=list(a1)
    a.sort()
    return a[-n:]

def repetidos(a):
    if len(set(a))==len(a):
        return False
    else:
        return True

def n_trapacas(n_jogadores,meta_repu):
    x=1-meta_repu
    return int(x*n_jogadores)

def ident_adv(reputacao_atual, reputacoes):
    reputacoes1=list(reputacoes)
    reputacoes1.sort()
    listinha=[]
    for i in range(len(reputacoes1)):
        if reputacoes1[i]==reputacoes1[i- 1]  and reputacoes1[i]!=reputacao_atual:
            listinha.append(reputacoes1[i])
    return listinha



class MeuJogador(Jogador):

    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        n_jogadores=len(reputacoes_dos_jogadores)
        escolhas=['c']*n_jogadores
        'criação'
        global listaRep
         
        arquivo = open('estrategias/ArquivoA.pck', 'wb')
        listaRep.append(round(reputacao_atual,12))
        pickle.dump(listaRep, arquivo)
        arquivo.close()
        
        
        
        meta_repu1=((float(numpy.mean(reputacoes_dos_jogadores))*0.45+0.15*float(max(reputacoes_dos_jogadores))+0.15*float(min(reputacoes_dos_jogadores)))+2.5)/6
        n_jogadores=len(reputacoes_dos_jogadores)
        escolhas=[]
        rep_max=3/4*comida_atual-3+3*float(numpy.mean(reputacoes_dos_jogadores))+1 #Antes de ser melhor do que a média eu quero estar vivo
        if rep_max<0:
            rep_max=0
        if rep_max>0.96:
            rep_max=0.95
        meta_repu=min([rep_max,meta_repu1]) #Isso aqui muda a meta de reputação se necessario
        descansos=int(n_trapacas(n_jogadores,meta_repu)) #Esse aqui determina quantas vezes eu preciso descansar pra atingir a minha meta
        descansos_bacana=int(descansos*0.8) #Esse daqui é uma versão legal para causar uma boa primeira impressão 
        ser_bacana=comida_atual/2-3*n_jogadores-5>0 #isso aqui me garante que ser bacana não causa problemas

        if rodada<3:
            escolhas=["d"]*n_jogadores
            for i in range(int(n_jogadores*6/7)):
                escolhas[i]='c'
                
            
        elif rodada<5: #nas 10 primeiras rodadas vou tentar farmar reputação
                escolhas=[]
                for i in range(0,n_jogadores):
                    if reputacoes_dos_jogadores[i] in n_melhores(reputacoes_dos_jogadores,int(descansos)):
                        escolhas.append("d")
                    else:
                        escolhas.append("c")

        elif rodada < 75:
            escolhas=[None]*n_jogadores
            for i in range(n_jogadores):
                if reputacao_atual>0.602:
                    escolhas[i]='d'
                else:
                    escolhas[i]=random.choice(['c','c','d','c'])

        elif rodada<100: #até a rodada 100, sem chances de ser bacana
            escolhas=[]
            for i in range(0,n_jogadores):
                if reputacoes_dos_jogadores[i] in n_melhores(reputacoes_dos_jogadores,int((1*descansos+3*n_jogadores)/4)):
                    escolhas.append("d")
                else:
                    escolhas.append("c")

                    
        else:
            escolhas=["d" for i in reputacoes_dos_jogadores]
        
        
            
    
                
                
        for i in range(n_jogadores):
            for j in range(len(ident_adv(reputacao_atual,reputacoes_dos_jogadores))):
                if reputacoes_dos_jogadores[i] - ident_adv(reputacao_atual,reputacoes_dos_jogadores)[j]<0.07:
                    if reputacoes_dos_jogadores[i]!= reputacao_atual:
                        escolhas[i]="d"
        
        
        
        if comida_atual-3*n_jogadores<300:
            escolhas=['d']*n_jogadores
        
        if rodada>10:
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
        
        