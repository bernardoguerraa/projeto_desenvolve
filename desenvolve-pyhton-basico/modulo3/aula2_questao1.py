#Juliana e Cris querem entrar em um bar, mas só podem se ambos forem maiores de idade (>17). 
#Escreva um programa que solicite as idades de Juliana e Cris e imprima True se ambas forem maiores de 17 anos, 
#indicando que podem entrar no bar, e False caso contrário.

idj= int(input("Qual a idade da Juliana:"))
idc= int(input("Qual a idade da Cris:"))
pode_entrar= idj>17 and idc>17
print(pode_entrar)