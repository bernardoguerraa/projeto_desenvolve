# Solicite uma frase do usuário e usando compreensão de listas imprima:

# A lista de vogais da frase, ordenada alfabeticamente

# A lista de consoantes da frase (remova espaços em branco)



# Solicitar frase do usuário
frase = input("Digite uma frase: ")

# Definir as vogais
vogais = ['a', 'e', 'i', 'o', 'u']

# Compreensão de listas para as vogais, ordenadas alfabeticamente
lista_vogais = sorted([letra for letra in frase.lower() if letra in vogais])
print("Lista de vogais (ordenada alfabeticamente):", lista_vogais)

# Compreensão de listas para as consoantes (remover espaços em branco)
lista_consoantes = [letra for letra in frase.lower() if letra.isalpha() and letra not in vogais]
print("Lista de consoantes (sem espaços em branco):", lista_consoantes)
