import re

arquivo_entrada = "frase.txt"
arquivo_saida = "palavras.txt"

# Ler o conteúdo do arquivo "frase.txt"
with open(arquivo_entrada, "r") as arquivo:
    conteudo = arquivo.read()

# Remover caracteres não alfabéticos e separar as palavras utilizando re findall
palavras = re.findall(r'\b[A-Za-zÀ-ÖØ-öø-ÿ]+\b', conteudo)

# Salvar cada palavra em uma nova linha no arquivo "palavras.txt"
with open(arquivo_saida, "w") as arquivo:
    for palavra in palavras:
        arquivo.write(palavra + "\n")

# Ler e imprimir o conteúdo do arquivo "palavras.txt"
with open(arquivo_saida, "r") as arquivo:
    conteudo_palavras = arquivo.read()
    print(conteudo_palavras)
