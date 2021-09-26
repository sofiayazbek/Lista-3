# Exercício 7

# DESAFIO (não obrigatório): Faça um algoritmo para ler 10 números e armazenar em uma lista. Após isto, o algoritmo deve ordenar os números na lista em ordem crescente. Escrever a lista ordenada.


numeros = []

for i in range(10):
  numero = int(input("Digite um número: "))
  numeros.append(numero)
print(numeros)

print(sorted(numeros))

