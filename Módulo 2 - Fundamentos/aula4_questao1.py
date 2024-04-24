largura = int(input("Digite a largura do terreno: "))
comprimento = int(input("Digite o comprimento do terreno: "))
preco_m2 = float(input("Digite o preço do m2: "))
area_m2 = largura*comprimento
preco_total = area_m2*preco_m2
print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.210f}.")