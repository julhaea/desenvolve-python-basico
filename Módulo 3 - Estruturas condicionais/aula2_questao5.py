genero = input("Digite 'M' para masculino e 'F' para feminino: ")
idade = int(input("Digite a idade: "))
tempodeservico = int(input("Digite o tempo de serviço: "))
aposentIdade = (genero == "M" and idade >=65) or (genero == "F" and idade >=60)
apostentIdadeServico = idade >= 60 and tempodeservico >= 25
aposentServico = tempodeservico >= 30
podeAposentar = aposentIdade or apostentIdadeServico or aposentServico
print(podeAposentar)