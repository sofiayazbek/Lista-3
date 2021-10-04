# Exercício 3

# Leia 5 números em uma lista. A seguir encontre o maior número digitado, apresentando para o usuário este número e a posição que ele se encontra na lista.


numeros = [1, 2, 3, 4, 5]
maior = 0
menor = 9999999
indice1 = 0
indice2 = 0

for i in range(5):
  if numeros[i] > maior:
    maior = numeros[i]
    indice1 = i
  if numeros[i] < menor:
    menor = numeros[i]
    indice2 = i
    


print(f"Os valores da lista são: {numeros}")
print(f"O maior número é: {maior}, e está na posição: {indice1}")
print(f"O menor número é: {menor}, e está na posição: {indice2}")