#Você está desenvolvendo um sistema de admissão para um clube juvenil de jogos de tabuleiro. Escreva um programa em Python que 
#pergunte ao usuário sua idade, se já jogou pelo menos 3 jogos de tabuleiro (resposta deve ser True ou False) e quantas vezes venceu 
#um jogo. O programa deve imprimir True, permitindo o ingresso do participante no clube, se:
#tiver entre 16 e 18 anos
#já tiver jogado pelo menos 3 jogos
#já ter vencido pelo menos 1 jogo, 


idade=int(input("Qual a sua idade? "))
jogou=bool(input("Ja jogoou pelo menos 3 jogos de tabuleiro? (responda com true ou false) "))
venceu=int(input("Quantas vezes ja venceu um jogo? "))
pode_participar= ((idade>15 and idade<19) and jogou and (venceu>0))
print("Pode entrar para o clube:", pode_participar)
