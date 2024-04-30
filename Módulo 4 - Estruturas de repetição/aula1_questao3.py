n1 = float(input("Primera nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
m = (n1 + n2 + n3) / 3
if m>=60:
    print("Aprovado")
elif m>=40:
    print("Recuperação")
else:
    print("Reprovado")
print('Fim')