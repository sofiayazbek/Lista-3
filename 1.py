# Exercício 1

# Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e armaze os nomes lidos em uma lista. Após isto, o algoritmo deve permitir a leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.


nomes = ["Joao", "Maria", "Pedro","Sofia", "Barbara", "Mariana", "Vitoria", "Paola", "Matheus", "Gustavo"]

print(nomes)

x = input("Digite um nome: ")

if x in nomes: 
  print(f"ACHEI - {x}")
else:
  print(f"NÃO ACHEI - {x}")


