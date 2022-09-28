class No:

    valor=0
    proximo_no=None
    anterior_no=None
    def __init__(self,valor):

        self.valor = valor


class Estrutura:

    no_inicio=None
    no_fim=None
    tamanho=0

    def adiciona(self,valor_do_no):
        no=No(valor_do_no)
        #primeiro nó que entra na pilha ele será o inicio e o fim
        if (self.no_inicio==None):
            self.no_inicio=no
            self.no_fim=no
            
        else:
            #próximo nó quando só tinha 1 primeiro
            if(self.no_fim==None):
                #O no de inicio aponta para o no fim que é o novo nó
                self.no_fim=no
                self.no_inicio.proximo_no=self.no_fim
                self.no_fim.anterior_no = self.no_inicio

            else:
                #Agora provavelmente já tem 2 nós ou mais e vai entrar mais um
                self.no_fim.proximo_no=no
                self.no_fim.proximo_no.anterior_no = self.no_fim
                self.no_fim=no
        self.tamanho+=1
    
    
class Pilha(Estrutura):

    def desempilha(self):
        no=None
        if(self.no_fim!=None):
            no=self.no_fim
            self.no_fim=self.no_fim.anterior_no
        else:
            print('Não existe nada na estrutura ainda')

        if(no!=None):
            return no.valor
        else:
            return None
            
class Fila(Estrutura):

    def desenfila(self):
        
        no=None
        if(self.no_inicio!=None):
            no=self.no_inicio
            self.no_inicio=self.no_inicio.proximo_no
        else:
            print('Não eixste nada na estrutura ainda')
        
        if(no!=None):
            return no.valor
        else:
            return None

class Lista(Estrutura):

    #percorre
    def listar_valores(self):
        
        if(self.no_inicio!=None):
            no = self.no_inicio
            while(no!=None):
                print(no.valor)
                no=no.proximo_no
        else:
            print('Lista vazia')
    
    #inseri na posição
    def inserir_na_posicao(self,posicao,valor):

        if (posicao>self.tamanho):
            print('Não existe essa posição na lista')
        else:
            no = self.no_inicio
            for lugar in range(posicao+1):
                no = no.proximo_no
            
            no_novo=No(valor)
            #não existe nó anterior, então o nó era o inicio
            if(no.anterior_no==None):
                #inicio aponta para novo nó,                
                self.no_inicio=no_novo
                #novo nó aponta para o antigo inicio
                no_novo.proximo_no = no
                # e o antigo nó do inicio aponta para o novo nó que agroa é o inicio
                no.anterior_no=no_novo
            if(no.proximo_no==None):
                #o no era o fim, então o fim aponta para novo nó
                self.no_fim=no_novo
                #o nó novo aponta seu anteriro para o antigo nó fim
                no_novo.anterior_no = no
                #e o antigo no fim  a aponta seu proximo para o novo no
                no.proximo_no = no_novo
            if((no.proximo_no!=None) & (no.anterior_no!=None)):
                #o nó anterior do no atual aponta com seu proximo para o no novo
                no.anterior_no.proximo_no = no_novo
                #o anteriro do novo nó aponta para o anterior
                no_novo.anterior_no = no.anterior_no
                #o proximo do nó novo aponta para no 
                no_novo.proximo_no = no
                # e o anterior de no aponto para no novo
                no.anterior_no=no_novo
            self.tamanho+=1



                
            
           

    #retira da posição


if (__name__=='__main__'):

    
    lista=Lista()
    lista.adiciona(1)
    lista.adiciona(2)
    lista.adiciona(3)

    lista.listar_valores()

    lista.inserir_na_posicao(2,5)
    lista.listar_valores()
   
