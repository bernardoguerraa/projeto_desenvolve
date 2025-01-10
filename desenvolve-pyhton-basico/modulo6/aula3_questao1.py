# Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), 
# os armazena em uma lista e, usando fatiamento de listas, imprima:

# A lista original

# Os 3 primeiros elementos

# Os 2 últimos elementos

# A lista invertida (do fim para o começo)

# Os elementos de índice par (0, 2, 4 … )

# Os elementos de índice ímpar (1, 3, 5, … )

numeros = []

qnt = int(input("Digite quantos números você quer colocar (No mínimo 4): "))

if qnt < 4:
    print("A quantidade deve ser no mínimo 4.")
    exit()  # Encerra o programa se a quantidade for menor que 4

for i in range (qnt):
    elementos = int(input("Digite os valores: "))
    numeros.append(elementos)

print(numeros)
print("Os tres primeiros elementos: " , numeros[0:3])
print("Os dois últimos elementos: " , numeros[-2:])
print("A lista invertida: " , numeros[::-1])
print("Elementos de ÍNDICE par:", numeros[::2])
print("Elementos de ÍNDICE ímpar:", numeros[1::2])
