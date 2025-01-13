import random

def encrypt(nomes):
    # Gerar a chave de criptografia aleatória entre 1 e 10
    chave = random.randint(1, 10)
    
    # Função para criptografar cada caractere de uma string
    def criptografar(nome, chave):
        criptografado = ""
        for c in nome:
            novo_char = chr((ord(c) + chave - 33) % (126 - 33 + 1) + 33)
            criptografado += novo_char
        return criptografado

    # Aplicar a criptografia em cada nome
    nomes_criptografados = [criptografar(nome, chave) for nome in nomes]
    
    return nomes_criptografados, chave

# Teste da função
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
nomes_cript, chave_aleatoria = encrypt(nomes)

print("Chave de criptografia:", chave_aleatoria)
print("Nomes criptografados:", nomes_cript)
