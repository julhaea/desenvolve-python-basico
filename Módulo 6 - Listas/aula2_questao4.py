num_elementos1 = int(input("Digite a quantidade de elementos que deseja colocar na primeira lista: "))
lista1 = []
print(f"Digite os {num_elementos1} elementos da lista 1: ")
for i in range(num_elementos1):
    x = int(input())
    lista1.append(x)
num_elementos2 = int(input("Digite a quantidade de elementos que deseja colocar na segunda lista: "))
lista2 = []
print(f"Digite os {num_elementos2} elementos da lista 2: ")
for i in range(num_elementos2):
    x = int(input())
    lista2.append(x)
if len(lista1)>len(lista2):
    listaMaior=lista1
    listaMenor=lista2
else:
    listaMaior=lista2
    listaMenor=lista1
listaIntercalada = []
for i in range(len(listaMenor)):
    listaIntercalada.append(lista1[i])
    listaIntercalada.append(lista2[i])
for i in range(len(listaMenor),len(listaMaior)):
    listaIntercalada.append(listaMaior[i])
print(listaIntercalada)

