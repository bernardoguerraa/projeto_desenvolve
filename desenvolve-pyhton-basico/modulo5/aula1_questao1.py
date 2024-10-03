numero1 = float(input("Insira o primeiro número decimal: "))
numero2 = float(input("Insira o segundo número decimal: "))

diferenca_absoluta = abs(numero1 - numero2)

resultado_arredondado = round(diferenca_absoluta, 2)

print("A diferença absoluta arredondada entre os dois números é:", resultado_arredondado)