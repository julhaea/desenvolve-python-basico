frase=input("Digite uma frase: ")
vogais="aeiouAEIOU"
for i in frase:
    if i in vogais:
        frase=frase.replace(i,"*")
print("Frase modificada: ",frase)   