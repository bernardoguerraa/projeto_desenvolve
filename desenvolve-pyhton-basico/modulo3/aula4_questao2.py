#Você está criando um sistema de classificação de filmes com base nas avaliações dos usuários. 
#Escreva um programa em Python que solicita ao usuário para inserir a avaliação de um filme em uma escala de 1 a 5. 

estrelas=int(input("Nota para o filme de 1 a 5: "))
if estrelas==5:
    print("Excelente!")
if estrelas==4:
    print("Muito bom!")
if estrelas==3:
    print("Bom!")
if estrelas==2:
    print("Regular!")
if estrelas==1:
    print("Ruim!")