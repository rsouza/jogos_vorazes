from estrategias.jogadores import Jogador

class MeuJogador(Jogador):
    
#objetivo de caduzinho:
#se manter vivo
#manter sua reputação em 0.6
#ajudar o outro

    def __init__(self):
        """
        Este metodo é executado quando o seu jogador for instanciado no início do jogo.
        
        Você pode adicionar outras variáveis a seu critério.
        
        Você não precisa definir comida ou reputação pois o Controlador do jogo vai manter o registro
        destas variáveis para cada jogador informando-as aos jogadores a cada rodada, através do método
        escolha_de_cacada.

        
        """
        self.comida = 0
        self.reputacao = 0
        self.historicocomida = []
        self.hiscacada = []
        
    def escolha_de_cacada(self, rodada, comida_atual, reputacao_atual, m, reputacoes_dos_jogadores):
        if rodada == 1:
            aux=len(reputacoes_dos_jogadores)//3
            aux1=len(reputacoes_dos_jogadores)-len(reputacoes_dos_jogadores)//3
            escolhas = ['d' for cadu in range(0,aux)]
            escolhas1 = ['c' for cadu in range(0,aux1)]
            escolhas = escolhas + escolhas1
            return escolhas
        elif rodada <= 100:
            escolhas = ['c' if cadu > 0.48 else 'd' for cadu in reputacoes_dos_jogadores]
            return escolhas
        elif rodada <= 400:
            escolhas = ['c' if cadu > 0.48 and cadu < 0.7 else 'd' for cadu in reputacoes_dos_jogadores]
            return escolhas
        else:
            escolhas = ['d' for cadu in reputacoes_dos_jogadores]
            return escolhas
            
            
       
        
    def resultado_da_cacada(self, comida_ganha):
        """
        este método é chamado depois que todas as cacadas da rodada forem terminadas.
        comida_ganha é uma lista com inteiros representando a comida ganha em cada uma das caçadas feitas na rodada. 
        Estes números podem ser negativos.
        
        Sua comida total é a soma destes números e a comida atual.
        
        adicione código para atualizar suas variáveis internas 
        """
        self.comida_ganha = comida_ganha

    def fim_da_rodada(self, recompensa, m, numero_de_cacadores):
        """
        Adicione código para alterar suas variaveis com base na cooperação que ocorreu na última rodada 
        recompensa: Comida total que você recebeu de jogadores que cooperaram na ultima rodada.
        numero_de_cacadores: inteiro que é o numero de caçadores que cooperou com você na última rodada.
        """
        #self.historico2[self.rodada] = (self.comida_ganha, recompensa, m, numero_de_cacadores)
        pass 
