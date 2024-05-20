titulo=input("Digite o título do livro: ")
autor=input("Digite o autor do livro: ")
ano=input("Digite o ano de publicação do livro: ")
numPag=input("Digite o número de páginas: ")
dados_livros=[titulo,autor,ano,numPag]
dados_livrosSTR=",".join(dados_livros)+"\n"
with open("meus_livros.csv","a",encoding="utf-8") as pl_livros:
    pl_livros.writelines(dados_livrosSTR)
