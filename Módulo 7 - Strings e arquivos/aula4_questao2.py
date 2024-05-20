with open("texto.txt","r") as arq_texto:
    palavras=arq_texto.read().split()
with open("frase.txt","w") as arq_palavras:
    for palavra in palavras:
        arq_palavras.write(palavra+"\n")
with open("frase.txt","r") as ler_palavras:
    print(ler_palavras.read())