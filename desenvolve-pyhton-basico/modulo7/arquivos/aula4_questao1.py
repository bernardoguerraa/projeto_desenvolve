import os

frase = input("Digite uma frase: ")

# Nome do arquivo
nome_arquivo = "frase.txt"

# Salvar a frase no arquivo
with open(nome_arquivo, "w") as arquivo:
    arquivo.write(frase)

# Obter o caminho completo do arquivo salvo
caminho_completo = os.path.abspath(nome_arquivo)

# Imprimir o caminho completo
print(f"Frase salva em {caminho_completo}")
