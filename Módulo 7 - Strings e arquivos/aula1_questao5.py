frase=input("Digite uma frase: ")
vogais="AEIOUaeiou"
num_vogais=0
indices_vogais=[]
for l in frase:
    if l in vogais:
        num_vogais+=1
        indices_vogais.append(frase.index(l))
print(f"{num_vogais} vogais")
print(f"Indíces: {indices_vogais}")

