classe = input("Escolha a classe (guerreiro, mago ou arqueiro): ")
pontosF = int(input("Digite os pontos de força (de 1 a 20): "))
pontosM = int(input("Digite os pontos de magia(de 1 a 20): "))
pode_guerreiro = classe == "guerreiro" and pontosF >= 15 and pontosM <= 10 and pontosF <= 20
pode_mago = classe == "mago" and pontosF <= 10 and pontosM >= 15 and pontosM <= 20
pode_arqueiro = classe == "arqueiro" and pontosF >= 5 and pontosF <=15 and pontosM <=15 and pontosM >= 5
pontosConsist = pode_mago or pode_arqueiro or pode_guerreiro
print(pontosConsist)