from datetime import datetime
data_hora = (datetime.now())
print(f"Data: {data_hora.strftime('%d/%m/%y')}")
print(f"Hora: {data_hora.strftime('%H:%M')}")
#faz o inverso
dia = int(input("Dia: "))
mes = int(input("Mês: "))
ano = int(input("Ano: "))
hora = int(input("Hora:"))
minuto = int(input("Minutos: "))
dataBag = f'{dia}/{mes}/{ano} {hora}:{minuto}'
data_for = datetime.strptime(dataBag, '%d/%m/%Y %H:%M')
print(data_for)