frase = "O meu amor mora em roma e me deu um ramo de flores"
objetivo = sorted("amor")

lst_palavras = frase.lower().split(" ") ## o .lower é para tirar as letras maiusculas e conseguir fazer a comparação e o split separa todas as palavras
for palavra in lst_palavras:
    if sorted(palavra) == objetivo:
        print(palavra)
