import random
import math
n = int(input("Digite a quantidade de números: "))
soma = 0
for i in range(n):
    x = random.randint(1,100)
    soma += x
raiz = math.sqrt(soma)
print(raiz)
