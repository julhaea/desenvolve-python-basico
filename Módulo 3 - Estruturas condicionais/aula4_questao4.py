dist = float(input("Digite a distância da entrega em Km: "))
peso = float(input("Digite o peso do pacote em Kg: "))
if dist <= 100:
    valor = peso
if dist > 100 and dist <= 300:
    valor = peso*1.5
if dist > 300:
    valor = peso*2
if peso > 10:
    valor = valor + 10
print(valor)