numero = input("Digite o número: ")

if len(numero) == 8:  # Se tiver apenas 8 dígitos
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":  # Se tiver 9 dígitos mas não começar com 9
    print("O número de celular deve começar com 9.")
    exit()

numero_formatado = numero[:5] + "-" + numero[5:]
print(f"Número completo: {numero_formatado}")

