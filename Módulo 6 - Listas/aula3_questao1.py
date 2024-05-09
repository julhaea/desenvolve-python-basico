num_elementos=int(input("Digite a quantidade de elementos que deseja colocar na lista: "))
lista=[]
print(f"Digite os {num_elementos} números da lista: ")
for i in range(num_elementos):
    x = int(input())
    lista.append(x)
print(lista)
print(lista[:3])
print(lista[-2:])
print(lista[::-1])
print(lista[::2])
print(lista[1::2])
