import random
num_elementos = random.randint(5,20)
elementos =[]
for i in range(num_elementos):
    elementos.append(random.randint(1,10))
soma_elementos = sum(elementos)
media_elementos = soma_elementos/num_elementos
print(elementos)
print(soma_elementos)
print(media_elementos)