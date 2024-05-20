from unidecode import unidecode
def maior_linha(linhas):
    maior_linha=""
    for linha in linhas:
        if len(linha)>len(maior_linha):
            maior_linha="".join(linha)
    return maior_linha
def linhas25(linhas):
    linhas_25lst=[]
    for i in range(25):
        linhas_25lst.append(linhas[i])
    linhas25str="\n".join(linhas_25lst)
    return linhas25str
def nonato(lst_palavras):
    n_nonato=0
    n_iria=0
    for palavra in lst_palavras:
        palavralw=palavra.lower()
        for letra in palavralw:
            if ord(letra)<97 or ord(letra)>122 and ord(letra)!=237:
                palavralw=palavralw.replace(letra,"")
        if palavralw=="nonato":
            n_nonato+=1
        if palavralw=="íria":
            n_iria+=1
    return print(f"Número de menções a Nonato: {n_nonato}\nNúmero de menções à Íria: {n_iria}")
with open("estomago.txt","r",encoding="utf-8") as roteiro:
    linhas=roteiro.read().split("\n")
with open("estomago.txt","r",encoding="utf-8") as roteiro:
    palavras=roteiro.read().split(" ")

n_linhas=len(linhas)
print(f"25 primeiras linhas: {linhas25(linhas)}")
print(f"Número de linhas: {n_linhas}")
print(f"Maior_linha: {maior_linha(linhas)}")
nonato(palavras)

