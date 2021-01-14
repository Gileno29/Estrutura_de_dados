li= [100,200,10,35,70,45]
size= len(li)
vezes=0

print('Lista inicial', li)
#implementation buble sort
for i in range(size):
    vezes=vezes+1
    change=False
    for j in range(1, size -i):
        if li[j]<li[j-1]:
            li[j], li[j-1] = li[j -1], li[j]
            change= True
    #print(vezes)
    if not change:
        break
print('lista final', li)
