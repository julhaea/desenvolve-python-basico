nExp = int(input("Digite o número de experimentos: "))
cont, sapo, rato, coelho, total = 0, 0, 0, 0, 0
while cont<nExp:
    cobaia = input("Qual tipo de cobaia foi utilizado no experimento (sapo, rato ou coelho)? ")
    quant = int(input("Quantas cobaias foram utilizadas? "))
    cont += 1
    if cobaia=="sapo":
        sapo += quant
        total += quant
    if cobaia=="rato":
        rato += quant
        total += quant
    if cobaia=="coelho":
        coelho += quant
        total += quant
porcSapo = sapo*100/total
porcRato = rato*100/total
porcCoelho = coelho*100/total
print(f"Total de cobaias: {total}.")
print(f"Total de sapos: {sapo}.")
print(f"Total de ratos: {rato}.")
print(f"Total de coelhos: {coelho}.")
print(f"Porcentagem sapos: {porcSapo:0.2f}%.")
print(f"Porcentagem ratos: {porcRato:0.2f}%.")
print(f"Porcentagem coelhos: {porcCoelho:0.2f}%.")
