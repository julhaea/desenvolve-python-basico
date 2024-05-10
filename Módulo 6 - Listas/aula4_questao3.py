horas_trabalhadas=[40,37,45,40,40,48]
pagamentos=[20*min(h,40) + 25*max(0,h-40) for h in horas_trabalhadas]
print(pagamentos)