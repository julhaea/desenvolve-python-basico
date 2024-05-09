import random
lista = []
for i in range(20):
    x = random.randint(-10,10)
    lista.append(x)
quant=0
listquant=[]
listaIndice=[]
indice=0
for i in lista:
    if i < 0:
        quant+=1
        listaIndice.append(indice)
        listquant.append(quant)
    else:
        quant=0
    indice+=1
indiceMaximo=listquant.index(max(listquant))
indUltimo= listaIndice[indiceMaximo]+1
tamOrdem= max(listquant)
inicioOrdem=indUltimo-tamOrdem
print(f"Original: {lista}")
del lista[inicioOrdem:indUltimo]
print(f"Editada: {lista}")
    
