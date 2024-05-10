frase=list(input("Digite uma frase: "))
vogais=["a","e","i","o","u", "A", "E","I","O","U"]
vogais_frase=[l for l in frase if l in vogais]
consoantes_frase=[l for l in frase if l not in vogais and l!=" "]
print(f"Vogais: {vogais_frase}")
print(f"Consoantes: {consoantes_frase}")