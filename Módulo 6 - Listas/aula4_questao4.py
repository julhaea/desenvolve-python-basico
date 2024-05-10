nomes=["Maria","José","Carla","Sol"]
notas=[35,50,20,80]
aprovados=[nomes[i] for i in range(len(nomes)) if notas[i]>=60]
print(aprovados)