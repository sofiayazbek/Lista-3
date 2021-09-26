# Exercício 5

# Faça um algoritmo para ler duas listas lista1 e lista2 de 5 números cada. Calcular e escrever a quantidade de vezes que lista1 e lista2 possuem os mesmos números  nas mesmas posições.


lista1=[2, 4, 6, 8, 10]
lista2=[3, 4, 7, 8, 10]

print(f"Os valores na lista 1 são: {lista1}")
print(f"Os valores na lista 2 são: {lista2}")

count = 0
for i in range(len(lista1)):
  if lista1[i] == lista2[i]:
    count=count+1
print(f"Existem {count} números iguais na mesma posição")


