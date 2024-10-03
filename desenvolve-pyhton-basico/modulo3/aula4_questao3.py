#Você está desenvolvendo um programa para verificar se um ano é bissexto. 
#Escreva um código em Python que solicita ao usuário para inserir um ano e imprime "Bissexto" se o ano for (1) divisível por 4 e 
#não for divisível por 100, ou (2) se for divisível por 400. Caso contrário, imprima "Não Bissexto".

ano=int(input("Digite o ano: "))
if ano%4==0 and ano%100!=0 or ano%400==0:
    print("Ano bissexto")
else:
    print("O ano não é bissexto")