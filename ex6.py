# Fac ̧a um programa que receba do usu ́ario um vetor com 10 posic ̧  ̃oes. Em seguida dever ́a
# ser impresso o maior e o menor elemento do vetor

vetor = []
i = 0

while i < 10:
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

    if i == 0:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    i += 1

print(f"O maior número fornecido é {maior} e o menor número fornecido é {menor}")
