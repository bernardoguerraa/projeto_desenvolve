import string

def validador_senha(senha):
    # Verifica se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        return False
    
    # Verifica se há pelo menos uma letra maiúscula
    if not any(char.isupper() for char in senha):
        return False
    
    # Verifica se há pelo menos uma letra minúscula
    if not any(char.islower() for char in senha):
        return False
    
    # Verifica se há pelo menos um número
    if not any(char.isdigit() for char in senha):
        return False
    
    # Verifica se há pelo menos um caractere especial
    caracteres_especiais = string.punctuation  # Obtém caracteres como @, #, $
    if not any(char in caracteres_especiais for char in senha):
        return False
    
    # Se passou por todas as verificações, a senha é válida
    return True

# Exemplos de uso
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"

print(validador_senha(senha1))  # Saída esperada: True
print(validador_senha(senha2))  # Saída esperada: False
print(validador_senha(senha3))  # Saída esperada: False
