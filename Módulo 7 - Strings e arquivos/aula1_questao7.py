import random
def encrypt(lista):
    chave=random.randint(0,10)
    nome=""
    for i in lista:
        nova_letra=chr(ord(i)+chave)
        nome+=nova_letra
    return nome



nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cripto=list(map(encrypt,nomes))
print("Nomes:",nomes)
chave=ord(nomes_cripto[0][0])-ord(nomes[0][0])
print("Chave aleatória:", chave)
print("Nomes criptografados:",nomes_cripto)
