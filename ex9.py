# Fac ̧a um programa que preencha um vetor com 10 n  ́umeros reais, calcule e mostre a
# quantidade de n  ́umeros negativos e a soma dos n  ́umeros positivos desse vetor.

vetor = []
i = 0
negativos = 0
soma = 0

while i < 10:
    numero = float(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)
    
    if numero < 0:
        negativos += 1    
    else:
        soma += numero
    i += 1

print(f"A quantidade de números negativos é {negativos} e a soma dos positivos é {soma}")