# Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. 
# Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. 
# Você deve imprimir a lista antes e depois da deleção.


import random

# Gerando a lista com 20 números aleatórios entre -10 e 10
lista = [random.randint(-10, 10) for _ in range(20)]

# Imprimindo a lista original
print("Lista original:", lista)

# Encontrando o intervalo com o maior número de números negativos
max_negativos = 0
inicio_intervalo = 0
fim_intervalo = 0

# Iterando sobre a lista para procurar o intervalo
for i in range(len(lista)):
    for j in range(i, len(lista)):
        # Sublista do intervalo
        intervalo = lista[i:j+1]
        # Contando os números negativos no intervalo
        num_negativos = sum(1 for x in intervalo if x < 0)
        
        # Atualizando o intervalo com maior quantidade de negativos
        if num_negativos > max_negativos:
            max_negativos = num_negativos
            inicio_intervalo = i
            fim_intervalo = j

# Deletando o intervalo da lista usando o operador del
del lista[inicio_intervalo:fim_intervalo+1]

# Imprimindo a lista após a deleção
print("Lista após a deleção:", lista)


# Utilizei dois loops para iterar sobre todos os intervalos possíveis da lista e contei quantos números negativos existem 
# em cada intervalo usando sum(1 for x in intervalo if x < 0).