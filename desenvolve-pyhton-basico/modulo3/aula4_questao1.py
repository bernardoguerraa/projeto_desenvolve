#Escreva um programa que lê dois números e informa se a sua soma é par ou ímpar.

num1= int(input("Digite o primeiro número: "))
num2=int(input("Digite o segundo número: "))
result=num1+num2
if result%2==0:
    print("A soma dos números é par")
if result%2==1:
    print(" A soma dos números é impar")