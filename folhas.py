class No :
    valor = None
    f_esq = None
    f_dir = None
    def __init__ ( self , valor , f_esq = None , f_dir = None ):
        self .valor = valor
        self .f_esq = f_esq
        self .f_dir = f_dir
    def __str__ ( self ):
        return str ( self .valor)

class ArvoreBinaria():

    def __init__(self, data):
        if data:
            no= No(data)
            self.root= no
        else:
            self.root= None

    def travessia_simetrica(self, no=None):
        if no is None:
            no= self.root
        if no.f_esq:
            self.travessia_simetrica(no.f_esq)
            print(no)
        if no.f_dir:
            self.travessia_simetrica(no.f_dir)
            print(no)
    def get(self, valor):
        if valor < self.valor:
            return self.valor.get(valor) if self.f_esq else None
        elif valor > self.valor:
            return self.f_dir.get(valor) if self.f_dir else None
        else:
            return self


if __name__=="__main__":
    tree = ArvoreBinaria(7)
    tree.root.f_esq=No(18)
    tree.root.f_dir=No(14)
    tree.root.f_dir=No(22)
    tree.root.f_dir=No(23)
    '''print(tree.root)
    print(tree.root.f_dir)
    print(tree.root.f_esq)'''
    tree.get(tree)
