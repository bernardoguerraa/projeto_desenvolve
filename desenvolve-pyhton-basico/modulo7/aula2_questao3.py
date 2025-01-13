import string

def eh_palindromo(frase):
    # Remove espaços, pontuação e deixa todas as letras em minúsculas
    frase_limpa = "".join(char.lower() for char in frase if char.isalnum())
    # Verifica se a frase limpa é igual à sua reversa
    return frase_limpa == frase_limpa[::-1]

while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    
    if frase.lower() == "fim":
        print("Programa encerrado.")
        break
    
    # Verifica se a frase é um palíndromo
    if eh_palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
