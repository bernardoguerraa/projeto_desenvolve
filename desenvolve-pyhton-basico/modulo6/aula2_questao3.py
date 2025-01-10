# Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. 
# Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:

# Ambas as listas

# A lista intersecção ordenada

# A quantidade de vezes que cada elemento aparece em cada lista

# Atenção, a lista de intersecções não pode ter duplicatas. 

import random

# Inicializando as listas
lista1, lista2, inter = [], [], []

# Preenchendo as listas com valores aleatórios
for _ in range(20):
    lista1.append(random.randint(0, 50))
    lista2.append(random.randint(0, 50))

# Exibindo as listas geradas
print("Lista 1:", lista1)
print("Lista 2:", lista2)

# Encontrando a interseção sem duplicatas
for elemento in lista1:
    if elemento in lista2 and elemento not in inter:
        inter.append(elemento)

# Ordenando a lista de interseção
inter.sort()

# Exibindo a lista de interseção e as contagens
print("\nLista Interseção (ordenada):", inter)
print("\nContagens:")
for elemento in inter:
    print(f"{elemento}: ({lista1.count(elemento)}, {lista2.count(elemento)})")
