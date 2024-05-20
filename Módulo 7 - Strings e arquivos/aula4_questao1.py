import os, sys
frs=input("Digite uma frase: ")
with open("texto.txt","a") as f:
    f.writelines(frs+"\n")
caminho=os.path.abspath("texto.txt")
print(f"Frase salva em: {caminho}")