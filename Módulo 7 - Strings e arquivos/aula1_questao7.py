import random
def encrypt(lista,chave):
    nome=""
    for i in lista:
        nova_letra=chr(ord(i)+chave)
        nome+=nova_letra
    return nome
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
chave=random.randint(0,10)
nomes_cripto=list(map(encrypt,nomes,[chave]*len(nomes)))
print("Nomes:",nomes)
print("Chave aleatória:", chave)
print("Nomes criptografados:",nomes_cripto)
