ano = int(input("Digite o ano: "))
bi1 = ano%4==0 and ano%100!=0
bi2 = ano%400==0
if bi1 or bi2:
    print(ano,"é um ano bissexto")
else:
    print(ano,"não é um ano bissexto")