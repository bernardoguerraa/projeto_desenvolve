#Escreva um programa que leia um valor inteiro referente a uma quantia em reais e calcule a 
#menor quantidade possível de notas necessárias para pagar aquele valor. As notas possíveis são: 
#100, 50, 20, 10, 5, 2, 1. 


valor=int(input("Digite o valor: "))
qnt_100= valor//100
valor= valor%100
qnt_50= valor//50
valor= valor= valor%50
qnt_20= valor//20
valor= valor= valor%20
qnt_10= valor//10
valor= valor= valor%10
qnt_5= valor//5
valor= valor= valor%5
qnt_2= valor//2
qnt_1= valor%2

print(f"Quantidade de notas:")
print(f" {qnt_100} nota(s) de 100")
print(f" {qnt_50} nota(s) de 50")
print(f" {qnt_20} nota(s) de 20")
print(f" {qnt_10} nota(s) de 20")
print(f" {qnt_5} nota(s) de 5")
print(f" {qnt_2} nota(s) de 2")
print(f" {qnt_1} nota(s) de 2")