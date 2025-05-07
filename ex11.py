# Fazer um programa para ler 5 valores e, em seguida, mostrar a posição onde se encon-
# tram o maior e o menor valor

vetor = []
i = 0

while i < 5:
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

    if i == 0:
        maior = numero
        posicao_maior = 0
        menor = numero
        posicao_menor = 0
    else:
        if numero > maior:
            maior = numero
            posicao_maior = i
        if numero < menor:
            menor = numero
            posicao_menor = i
    i += 1

print(f"O maior número é {maior} e está na posição {posicao_maior}, já o menor número é {menor} e está na posição {posicao_menor}")