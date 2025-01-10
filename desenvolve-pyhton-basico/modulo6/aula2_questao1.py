#Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. 
# Em seguida imprima na ordem estabelecida: A lista ordenada, sem modificar a lista original
# A lista original
#O índice do maior valor da lista
#O índice do menor valor da lista

import random #biblioteca para gerar numeros aleatorios

aleatorios = [] #inicializei a ista vazia
for i in range(20):
    valores = random.randint(-100,100)
    aleatorios.append(valores) #append adiciona valores a lista

## aleatorios.sort ALTERA a lista original

print(sorted(aleatorios)) #gerou uma copia da lista sorteando de novo os numeros (nao alterou a original)
print(aleatorios) #exibe a lista original
print("O maior valor esta no indice:",aleatorios.index(max(aleatorios)))
print("O menor valor esta no indice:", aleatorios.index(min(aleatorios)))