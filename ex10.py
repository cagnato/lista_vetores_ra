# Fazer um programa para ler 5 valores e, em seguida, mostrar todos os valores lidos
# # juntamente com o maior, o menor e a média dos valores.

vetor = []
i = 0
soma = 0

while i < 5:
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
    soma += numero    
    i += 1

media = soma / 5

print(f"Os valores informados são {vetor}, o maior número informado é {maior}, o menor número informado é {menor}, e por fim a média dos números informados é {media}")