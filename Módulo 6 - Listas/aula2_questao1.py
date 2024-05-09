import random
lista = []
for i in range(20):
    lista.append(random.randint(-100,100))
print(sorted(lista))
print(lista)
print(f"O maior valor está no índice {lista.index(max(lista))}")
print(f"O menor valor está no índice {lista.index(min(lista))}")