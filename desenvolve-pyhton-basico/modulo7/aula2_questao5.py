import random

def embaralhar_palavras(frase):
    def embaralhar_palavra(palavra):
        # Se a palavra tiver menos de 4 caracteres, não é possível embaralhar internamente
        if len(palavra) <= 3:
            return palavra
        # Mantém a primeira e última letra fixas, embaralhando as letras internas
        meio = list(palavra[1:-1])
        random.shuffle(meio)
        return palavra[0] + ''.join(meio) + palavra[-1]

    # Divide a frase em palavras, embaralha cada palavra e junta novamente
    palavras = frase.split()
    palavras_embaralhadas = [embaralhar_palavra(palavra) for palavra in palavras]
    return ' '.join(palavras_embaralhadas)

# Exemplo de uso
frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
