import random

# Função para imprimir o enforcado
def imprime_enforcado(erros):
    with open("gabarito_enforcado.txt", "r", encoding="utf-8") as f:
        estagios = f.read().split("=========\n")
        print(estagios[erros])

# Escolher uma palavra aleatória
with open("gabarito_forca.txt", "r", encoding="utf-8") as f:
    palavras = f.read().splitlines()
    palavra_secreta = random.choice(palavras).lower()

# Configuração inicial do jogo
palavra_descoberta = ["_"] * len(palavra_secreta)
letras_tentadas = set()
erros = 0
tentativas_max = 6

print("Bem-vindo ao jogo da forca!")
print(" ".join(palavra_descoberta))

# Loop principal do jogo
while erros < tentativas_max and "_" in palavra_descoberta:
    letra = input("\nDigite uma letra: ").lower()
    
    if not letra.isalpha() or len(letra) != 1:
        print("Digite apenas uma letra!")
        continue

    if letra in letras_tentadas:
        print("Você já tentou essa letra!")
        continue

    letras_tentadas.add(letra)

    if letra in palavra_secreta:
        print("Você acertou!")
        for i, l in enumerate(palavra_secreta):
            if l == letra:
                palavra_descoberta[i] = letra
    else:
        print("Você errou!")
        erros += 1
        imprime_enforcado(erros)
    
    print("\nProgresso:", " ".join(palavra_descoberta))
    print("Letras tentadas:", ", ".join(sorted(letras_tentadas)))

# Final do jogo
if "_" not in palavra_descoberta:
    print("\nParabéns, você venceu! A palavra era:", palavra_secreta)
else:
    imprime_enforcado(erros)
    print("\nVocê perdeu! A palavra era:", palavra_secreta)
