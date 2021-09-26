# Exercício 3

# Leia 5 números em uma lista. A seguir encontre o maior número digitado, apresentando para o usuário este número e a posição que ele se encontra na lista.


numeros = [1, 2, 3, 4, 5]
maior = 0
menor = 9999999

for i in range(5):
  if numeros[i] > maior:
    maior = numeros[i]
  if numeros[i] < menor:
    menor = numeros[i]


print(f"Os valores da lista são: {numeros}")
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")