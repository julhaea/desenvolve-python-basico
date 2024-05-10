lista=[n for n in range(1,101)]
pares20_50=[n for n in lista if n>=20 and n<=50 and n%2==0]
quadrados=[n**2 for n in lista[:9]]
div7=[n for n in lista if n%7==0]
par_impar=["par" if n%2==0 else "impar" for n in lista[0:30:3]]
print(pares20_50)
print(quadrados)
print(div7)
print(par_impar)