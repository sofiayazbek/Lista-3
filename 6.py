# Exercício 6

# Faça um algoritmo para ler uma lista de 5 números. Após isto, ler mais um número qualquer, calcular e escrever quantas vezes esse número aparece na lista.


lista = [1, 2, 3, 4, 5]
num = lista.append(int(input(f"Digite um número qualquer: ")))

print(f"{lista}")


quant = lista.count(lista[5])

print(f"O valor {lista[5]} aparece {quant} vezes na lista")




