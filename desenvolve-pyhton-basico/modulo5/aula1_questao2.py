import random
import math

n = int(input("Insira o valor de n: "))
soma = 0 
for i in range(n):
    valor = random.randint (0,100)
    print(valor)
    soma = soma + random.randint (0,100)
print(soma)
print("A raiz quadrada é:", math.sqrt (soma))