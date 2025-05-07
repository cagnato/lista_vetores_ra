# Leia um vetor de 10 posic ̧ ̃oes. Contar e escrever quantos valores pares ele possui

vetor = []
i = 0
pares = 0

while i <= 9:
    numero = int(input(f"Digite o {i+1}º número: "))
    vetor.append(numero)

    if numero % 2 == 0:
        pares +=1
    i += 1

print(f"O total de números pares é {pares}")