import random
lista1= []
lista2= []
for i in range(20):
    lista1.append(random.randint(0,50))
    lista2.append(random.randint(0,50))
def funcInter(a,b):
    inter=[]
    for n in a:
        if n in b:
            inter.append(n)
    return sorted(set(inter))
interseccao = funcInter(lista1,lista2)
print(lista1)
print(lista2)
print(interseccao)
for elemt in interseccao:
    q1=lista1.count(elemt)
    q2=lista2.count(elemt)
    print(f"{elemt}: (lista1={q1}, lista2={q2})")