nAlunos = int(input("Quantos alunos?"))
n = 0
idades = 0
while n<nAlunos:
    idade = int(input("Digite a idade de um aluno: "))
    idades += idade
    n+=1
media=idades/nAlunos
print(media)