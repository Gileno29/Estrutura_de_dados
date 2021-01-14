#busca binária em python

class Buscador:

    def __init__(self, li, element):
        self.li= li
        self.first=0
        self.last=len(li)-1
        self.element=element

    def busca_binaria(self):
        #print('entrei')
        search_element= self.element
        #print(search_element)
        while(self.first <= self.last):
            mid=(self.first+ self.last)//2
            element= self.li[mid]

            if  element< search_element:
                self.first = mid + 1

            elif  element> search_element:
                self.last = mid-1

            else:
                return mid

        return "element not found"

li=[10,20,30,40,50]

b= Buscador(li, 30)
print(b.busca_binaria())
