#Você está implementando um sistema de entrega expressa e precisa calcular o valor do frete com base na distância e no peso do pacote.]

#Distância até 100 km: R$1 por kg.
#Distância entre 101 e 300 km: R$1.50 por kg.
#Distância acima de 300 km: R$2 por kg.
#Acrescente uma taxa de R$10 para pacotes com peso superior a 10 kg

dist=float(input("Digite a distância em km: "))
peso=float(input("Digite o peso do pacote em kg: "))
preço=0

if dist<101:
    if peso>10:
        print(f"O preço do frete é R${peso+10:.2f}")
    else:
        print(f"O preço do frete é R${peso:.2f}")
if dist>100 and dist<301:
    preço=peso*1.50
    if peso>10:
        print(f"O preço do frete é R${preço+10:.2f}")
    else:
        print(f"O valor do frete é R${preço:.2f}")
if dist>300:
    preço=peso*2
    if peso>10:
        print(f"O preço do frete é R${preço+10:.2f}")
    else:
        print(f"O valor do frete é R${preço:.2f}")