# Exercício 2

# Escreva um algoritmo que permita a leitura das notas de uma turma de 5 alunos, armazenando os dados numa lista. Depois calcule a média da turma e conte quantos alunos obtiveram nota acima desta média calculada. Escrever a média da turma e o resultado da contagem.


numeros = []

for i in range(5):
  numero = int(input("Digite um número: "))
  numeros.append(numero)

soma = 0
for numero in numeros:
  soma = soma + numero 

for numero in numeros:
  print(numero)

media = 0
for numero in numeros:
  media = soma/5

print(f"A média dos alunos foi: {media}")






