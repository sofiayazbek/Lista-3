# Exercício 4

# Faça um algoritmo para ler 5 números e armazenar em uma lista. Após a leitura, o algoritmo deve escrever esses 5 números lidos na ordem inversa.


numeros = []

for i in range(1, 6):
  num = int(input(f"Digite um número para a posição {i}: "))
  numeros.append(num)
print(f"Os valores digitados foram: {numeros}")

numeros = numeros[::-1]

print(f"Os valores digitados na ordem inversa são: {numeros}")
