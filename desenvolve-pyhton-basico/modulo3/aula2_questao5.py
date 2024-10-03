#Solicite de um usuário seu gênero ("M" ou "F"), sua idade e seu tempo de serviço (em anos) e escreva uma expressão que imprima 
#True se a pessoa já pode se aposentar, ou False caso contrário, de acordo com as seguintes regras:
#A: Para mulheres, ter mais de 60 anos. Para homens, 65.
#B: Ou ter trabalhado pelo menos 30 anos
#C: Ou ter 60 anos  e trabalhado pelo menos 25.

genero=input("Genero (M ou F): ")
idade=int(input("Idade: "))
t_serviço=int(input("Quantos anos de serviço: "))

aposentar= ((genero=='F' or genero=='f') and idade>60) \
        or ((genero =='M' or genero== 'm') and idade>65) \
        or (t_serviço>29) \
        or (idade>59 and t_serviço>24)

print("Você pode aposentar: ", aposentar)