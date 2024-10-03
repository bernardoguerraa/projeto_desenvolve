#Você está desenvolvendo um programa para calcular o preço total de uma compra em uma loja online. O preço dos produtos é 
#calculado multiplicando a quantidade pelo preço unitário. Escreva um programa em Python que solicite do usuário o nome, o 
#preço unitário e a quantidade de 3 produtos comprados e imprima ao final o preço total da compra.

p1= input("Digite o nome do produto 1:") 
preço_p1= float(input("Digite o preço unitário do produto 1:")) 
qnt_p1= int(input("Digite a quantidade do produto 1:")) 
p2=input("Digite o nome do produto 2:") 
preço_p2=float(input("Digite o preço unitário do produto 2:"))
qnt_p2= int(input("Digite a quantidade do produto 2:")) 
p3= input("Digite o nome do produto 3:")
preço_p3= float(input("Digite o preço unitário do produto 3:"))
qnt_p3= int(input("Digite a quantidade do produto 3:")) 

preço_final=(preço_p1*qnt_p1)+(preço_p2*qnt_p2)+(preço_p3*qnt_p3)
print(f"Total: R${preço_final:,.2f}")