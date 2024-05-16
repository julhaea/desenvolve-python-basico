while 1>0:
    frase=input("Digite uma frase(ou digite 'Fim' para encerrar): ")
    frase_invertida=frase[::-1]
    f=(frase.replace(" ","")).lower()
    fi=(frase_invertida.replace(" ","")).lower()
    if frase=="Fim":
        break
    if f==fi:
        print(f"'{frase}' é um palíndromo")
    else:
        print(f"'{frase}' não é um palíndromo")


