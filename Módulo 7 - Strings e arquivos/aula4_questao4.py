import random
with open("gabarito_forca.txt","r") as gabarito:
    linha=random.randint(1,10)
    linhaI=1
    for palavra in gabarito:
        if linhaI==linha:
            palavra_gabarito=palavra
            break
        linhaI+=1
with open("gabarito_enforcado.txt","r") as arq_forcas:
    forcas=arq_forcas.read().split("\n\n")
underscore="_"*(len(palavra_gabarito)-1)
def play_forca(forca,erros):
    return forca[erros]
print(f"Palavra:", " ".join(underscore))
erros=0
underscorelst=list(underscore)
resposta=""
while 1>0:
    resposta="".join(underscorelst)+"\n"
    if resposta==palavra_gabarito:
        print("Você venceu!")
        break
    if erros>5:
        print("Você perdeu!")
        break
    tent_letra=input("Digite uma letra: ")
    if tent_letra in palavra_gabarito:
        i=0
        for letra in palavra_gabarito:
            if letra==tent_letra:
                underscorelst[i]=letra
            i+=1
    else:
        erros+=1
    print("\n")
    print(play_forca(forcas,erros))
    print(" ".join(underscorelst),"\n")
    

