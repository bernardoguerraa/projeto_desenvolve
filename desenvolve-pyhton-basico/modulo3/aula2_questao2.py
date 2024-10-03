#Dando continuidade à questão anterior, um outro bar permite a entrada de grupos onde pelo menos uma pessoa é maior de idade 
#(ficando responsável pelas outras). Ajuste sua resposta da questão anterior, ainda solicitando as idades de Juliana e Cris, 
#mas ajustando a expressão para esse novo cenário, imprimindo True se puderem entrar no bar, e False caso contrário.


idj= int(input("Qual a idade da Juliana:"))
idc= int(input("Qual a idade da Cris:"))
pode_entrar= idj>17 or idc>17
print(pode_entrar)