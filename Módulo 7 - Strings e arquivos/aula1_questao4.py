numero=input("Digite o seu número: ")
num_completo=0
if len(numero)==8:
    num_completo="9"+numero
elif len(numero)>9 or len(numero)<9 or numero[0]!="9":
    print("Número inválido")
else:
    num_completo=numero
if num_completo!=0:
    i=0
    num_pronto=""
    for n in num_completo:
        num_pronto+=n
        i+=1
        if i==5:
            num_pronto+="-"
    print(f"Número completo: {num_pronto}")

   
