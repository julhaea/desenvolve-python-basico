frase=input("Digite uma frase: ")
palavra_objetivo=sorted(input("Digite a palavra objetivo:"))
lista_palavras=(frase.lower()).split()
anagramas=[]
for palavra in lista_palavras:
    if sorted(palavra)==palavra_objetivo:
        anagramas.append(palavra)
print("Anagramas:",anagramas)
