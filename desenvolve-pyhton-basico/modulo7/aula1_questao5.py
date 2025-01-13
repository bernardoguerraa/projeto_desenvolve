frase = "O meu amor mora em roma e me deu um ramo de flores"

count_vogais = 0
indices = []

for i in range(len(frase)):
    if frase[i] in "aeiouAEIOU":
        count_vogais += 1
        indices.append(i)

print("Número de vogais na frase: ", count_vogais)
print(indices)