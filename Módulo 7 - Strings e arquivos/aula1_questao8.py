CPF=input("Digite seu CPF: ")
listaCPF=[int(i) for i in CPF if i!="." and i!="-"]
def validador(CPF):
    multiplicador=10
    soma1=0
    for i in CPF[:9:1]:
        x=i*multiplicador
        soma1+=x
        multiplicador-=1
    if soma1%11<2:
        digito1=0
    else:
        digito1=11-(soma1%11)
    soma2=0
    multiplicador=11
    for i in CPF[:9:1]:
        x=i*multiplicador
        soma2+=x
        multiplicador-=1
    soma2+=digito1*multiplicador
    if soma2%11<2:
        digito2=0
    else:
        digito2=11-(soma2%11)
    if CPF[9]==digito1:
        if CPF[10]==digito2:
            return print("CPF válido")
        else:
            return print("CPF inválido")
    else:
        return print("CPF inválido")
validador(listaCPF)