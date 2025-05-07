# Escreva um programa que leia 10 n  ́umeros inteiros e os armazene em um vetor. Imprima
# o vetor, o maior elemento e a posic ̧ ̃ao que ele se encontra

vetor = []
i = 0

while i < 10:
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

    if i == 0:
        maior = numero
        posicao_maior = 0
    else:
        if numero > maior:
            maior = numero
            posicao_maior = i
    i += 1

print(f"O maior número é {maior} e está na posição {posicao_maior}")