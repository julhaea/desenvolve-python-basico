meses=["Janeiro","Fevereiro","Março","Abril","Maio","Junho","Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
data=input("Digite sua data de nascimento (dd/mm/aaaa):")
data_separada=data.split("/")
data_pronta="".join(f"{data_separada[0]} de {meses[(int(data_separada[1])-1)]} de {data_separada[2]}")
print(data_pronta)