
class Ordenador:
    
    def __init__(self):
        self.li= [100,200,10,35,70,45]
        self.size= len(self.li)
        self.vezes=0

    def buble_sort(self):
        print('Lista inicial', self.li)
        #implementation buble sort
        for i in range(self.size):
            self.vezes=self.vezes+1
            change=False
            for j in range(1, self.size -i):
                if self.li[j]<self.li[j-1]:
                    self.li[j], self.li[j-1] = self.li[j -1], self.li[j]
                    change= True
            #print(vezes)
            if not change:
                break
        print('lista final', self.li)

o= Ordenador()
o.buble_sort()
