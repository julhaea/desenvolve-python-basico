import random
def embaralhar_frase(frase):
    palavras = frase.split()
    palavras_embaralhadas = []
    for palavra in palavras:
        if len(palavra)>1:
            primeiraLetra = palavra[0]
            letrasInternas = list(palavra[1:-1])
            random.shuffle(letrasInternas)
            ultimaLetra = palavra[-1]
            palavra_embaralhada = primeiraLetra + ''.join(letrasInternas) + ultimaLetra
            palavras_embaralhadas.append(palavra_embaralhada)
        else:
            palavras_embaralhadas.append(palavra)
    frase_embaralhada =' '.join(palavras_embaralhadas)
    return frase_embaralhada
frase = input("Digite uma frase: ")
print(embaralhar_frase(frase))