idade = int(input("Digite sua idade: "))
_3jogos = input("Já jogou pelo menos 3 jogos de tabuleiro? Responda 'True' para sim e 'False' para não.")
mais3jogos = bool(_3jogos=="True")
vitorias = int(input("Quantas vezes já venceu um jogo? "))
print(bool((idade>=16 and idade<=18)and(mais3jogos)and(vitorias>0)))