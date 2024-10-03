#Faça um programa para ler as dimensões de um terreno em inteiros (comprimento e largura), bem como o preço do metro quadrado da 
#região em ponto flutuante. Calcule o valor do terreno e imprima o resultado com a formatação apresentada a seguir.

#O terreno possui 250m2 e custa R$512,490.50

#Comente na linha acima de cada instrução uma breve descrição da instrução.

#Fórmulas:
#area_m2 = comprimento * largura
#preco_total = preco_m2 * area_m2


comprimento= int(input("Digite o comprimento: "))
largura= int(input("Digite a largura: "))
preco_m2= float(input("Digite o preço do metro quadrado: "))
area= comprimento*largura #calculo da area em m2
preco= area*preco_m2 #preço total
print(f"O terreno possui {area}m2 e custa R${preco:,.2f}")