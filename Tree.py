class No:

     def __init__(self, valor, dir, esq):
          self.item = valor
          self.dir = dir
          self.esq = esq

class Tree:

     def __init__(self):
          self.root = None
     def inserir(self, v):
          novo = No(v,None,None)
          if self.root == None:
               self.root = novo
          else:
               atual = self.root
               while True:
                    anterior = atual
                    if v <= atual.item:
                         atual = atual.esq
                         if atual == None:
                                anterior.esq = novo
                                return
                    else:
                         atual = atual.dir
                         if atual == None:
                                 anterior.dir = novo
                                 return

     def buscar(self, chave):
         if self.root == None:
              return None # se arvore vazia
         atual = self.root # começa a procurar desde raiz
         while atual.item != chave: # enquanto nao encontrou
               if chave < atual.item:
                    atual = atual.esq # caminha para esquerda
               else:
                    atual = atual.dir # caminha para direita
               if atual == None:
                    return None # encontrou uma folha -> sai
         return atual

#Exibindo em Ordem erd e erd
     def erd(self, atual):
         if atual != None:
              self.erd(atual.esq)
              print(atual.item,end=" ")
              self.erd(atual.dir)

     def red(self, atual):
         if atual != None:
              print(atual.item,end=" ")
              self.red(atual.esq)
              self.red(atual.dir)



    #Calcula a altura
     def altura(self, atual):
          if atual == None or atual.esq == None and atual.dir == None:
               return 0
          else:
             if self.altura(atual.esq) > self.altura(atual.dir):
                return  1 + self.altura(atual.esq)
             else:
                return  1 + self.altura(atual.dir)


     def caminhar(self):
          print(" Exibindo em erd: ",end="")
          self.erd(self.root)
          print("\n Exibindo em red: ",end="")
          self.red(self.root)
          print("\n Altura da arvore: %d" %(self.altura(self.root)))


arv = Tree()
print("Arvore Binaria")
opcao = 0
while opcao != 5:
     print("***********************************")
     print("Entre com a opcao:")
     print(" --- 1: Inserir")
     print(" --- 2: Pesquisar")
     print(" --- 3: Exibir")
     print(" --- 4: Sair do programa")
     print("***********************************")
     opcao = int(input("-> "))
     if opcao == 1:
          x = int(input(" Informe o valor -> "))
          arv.inserir(x)
     elif opcao == 2:
          x = int(input(" Informe o valor -> "))
          if arv.buscar(x) != None:
               print(" Valor Encontrado")
          else:
               print(" Valor nao encontrado!")
     elif opcao == 3:
          arv.caminhar()
     elif opcao == 4:
          break
