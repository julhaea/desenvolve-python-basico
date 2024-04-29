n1 = int(input("Digite o primeiro valor da soma: "))
n2 = int(input("Digite o segundo valor da soma: "))
valor = (n1+n2)%2
print("A soma dos dois números resulta em um número par" if valor == 0 else "A soma dos dois números resulta em um número ímpar")
