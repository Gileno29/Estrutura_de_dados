from No import No

class ListaLigada:

    def __init__(self):
        self.cabeca=None
        self.tamanho=0


    def adicionar(self, elemento):

        if(self.cabeca):
            aux= self.cabeca
            while (aux.proximo):
                aux= aux.proximo
            aux.proximo= No(elemento)
        else:
            self.cabeca= No(elemento)
        self.tamanho= +1

    def __len__(self):
        return self.tamanho

    def get(self, index):
        pass
    def set(self, index, elemento):
        pass

    def  __getitem__(self, index):
        aux= self.head
        for i in range(index):
            if(aux):
                aux= aux.next
            else:
                raise IndexError("Index fora da lista de elementos")
        if aux:
            return aux.dado
        raise IndexError("Index fora do tamanho da lista")

        def __setitem__(self, index, elemento):
            aux= self.head
            for i in range(index):
                if(aux):
                    aux= aux.next
                else:
                    raise IndexError("Index fora da lista de elementos")
            if aux:
                 aux.dado= elemento
            else:
                raise IndexError("Index fora do tamanho da lista")
        def procura(self, elemento):
            aux= self.cabeca
            i= 0
            while (aux):
                if aux.dado== elemento:
                    return i
                aux= aux.proximo
                i= i+1
