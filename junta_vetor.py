
vet_1=[1,2,3,4,5,5]
vet_2=[3,4,5,6]




def juntar(v1, v2):
    result=set(vet_1).intersection(vet_2)
    print(type(set(vet_1)))
    print(result)

juntar(vet_1, vet_2)

print('funcionou')
