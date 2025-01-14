import re

# Nome do arquivo contendo o roteiro
arquivo = "estomago.txt"

# Abrindo o arquivo para leitura
with open(arquivo, "r", encoding="utf-8") as f:
    linhas = f.readlines()

# 1. Texto das primeiras 25 linhas
print("Texto das primeiras 25 linhas:")
for linha in linhas[:25]:
    print(linha.strip())

# 2. Número total de linhas no arquivo
numero_linhas = len(linhas)
print("\nNúmero total de linhas no arquivo:", numero_linhas)

# 3. Linha com o maior número de caracteres
linha_mais_longa = max(linhas, key=len)
print("\nLinha com o maior número de caracteres:")
print(linha_mais_longa.strip())

# 4. Contar menções a "Nonato" e "Íria" (case insensitive, sem incluir "iria" em outras palavras)
texto_completo = "".join(linhas)
menções_nonato = len(re.findall(r'\bnonato\b', texto_completo, re.IGNORECASE))
menções_iria = len(re.findall(r'\bíria\b', texto_completo, re.IGNORECASE))

print("\nNúmero de menções aos personagens:")
print(f"Nonato: {menções_nonato}")
print(f"Íria: {menções_iria}")
