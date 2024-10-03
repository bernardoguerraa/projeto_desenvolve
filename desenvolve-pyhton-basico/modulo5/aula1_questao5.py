import emoji

# Dicionário de emojis disponíveis com seus códigos
emojis = {
    ':red_heart:': '❤️',
    ':thumbs_up:': '👍',
    ':thinking_face:': '🤔',
    ':partying_face:': '🥳'
}

# Apresenta a lista de emojis disponíveis com o texto correspondente
print("Emojis disponíveis:")
for emoji_code, emoji_symbol in emojis.items():
    print(f"{emoji_symbol} - {emoji_code}")

# Solicita uma frase codificada ao usuário
frase_codificada = input("\nDigite uma frase e ela será emojizada: ")

# Decodifica a frase utilizando a função emoji.emojize()
frase_emojizada = emoji.emojize(frase_codificada, use_aliases=True)

# Apresenta a frase emojizada
print("Frase emojizada:")
print(frase_emojizada)