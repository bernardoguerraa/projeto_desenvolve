#Você é mestre de uma mesa de RPG e vai criar um sistema para validar uma ficha de personagem. 
#Cada personagem tem uma classe específica com requisitos de atributos. Escreva um script que solicita a classe de personagem 
#escolhida (guerreiro, mago ou arqueiro), os pontos de força e os pontos de magia atribuídos ao personagem. 
#O programa deve imprimir True se os pontos de atributo são consistentes com a classe escolhida, seguindo as seguintes regras:

#Guerreiro: Força deve ser igual ou superior a 15, Magia deve ser 10 ou menos.
#Mago: Força deve ser 10 ou menos, Magia deve ser igual ou superior a 15.
#Arqueiro: Força e Magia devem ser ambos superiores a 5, mas nenhum deles pode ser superior a 15.

personagem=input("Qual a classe do seu personagem (guerreiro, mago ou arqueiro)? ")
força=int(input("Quantos pontos de força ele tem? "))
magia=int(input("Quantos pontos de magia ele tem? "))

valido=(personagem=="guerreiro" and força>14 and magia<11) or (personagem=="mago" and força<11 and magia>14) or (personagem=="arqueiro" and força>5 and magia>5 and força<16 and magia<16)

print("Seu personagem é válido:" , valido)