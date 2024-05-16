def validador_de_senha(senha):
    chr_esp=0
    num=0
    l_ma=0
    l_mi=0
    if len(senha)>=8:
        for i in senha:
            x=ord(i)
            if x>=33 and x<=47 or x>=58 and x<=64 or x>=91 and x<=96 or x>=123 and x<=126: chr_esp+=1
            if x>=48 and x<=57: num+=1
            if x>=65 and x<=90: l_ma+=1
            if x>=97 and x<=122: l_mi+=1
        if chr_esp>0 and num>0 and l_ma>0 and l_mi>0:
            return True
        else: return False
    else:
        return False
senha=input("Digite sua senha: ")
print(validador_de_senha(senha))