import datetime

# Obter a data e hora atuais
data_hora_atual = datetime.now()

# Formatar a data e hora
data_formatada = data_hora_atual.strftime("%d/%m/%Y")
hora_formatada = data_hora_atual.strftime("%H:%M")

# Exibir a data e hora formatadas
print("Data:", data_formatada)
print("Hora:", hora_formatada)

#o método strftime() para formatar a data e hora atuais de acordo com o padrão