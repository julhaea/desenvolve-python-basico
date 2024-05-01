import random
x = random.randint(1,10)
while 1>0:
    resp = int(input("Tente acertar um número de 1 a 10: "))
    if resp == x:
        print("Você acertou!")
        break
    if resp > x:
        print("O número é menor")
    if resp < x:
        print("O número é maior")
