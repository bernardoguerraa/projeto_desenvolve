#Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. 
#Escreva um programa que leia um inteiro N com a quantidade de respondentes e em seguida leia as N idades de cada respondente. 
#Ao final, imprima a média das idades.

n = int (input("Digite o núemro de respondentes:"))
soma=0
x = n 

while n > 0:
    id=int(input("Qual a sua idade:"))
    soma= soma + id
    n = n - 1 

media = soma / x
print (f"A media das idades é: {media:.2f}")
    