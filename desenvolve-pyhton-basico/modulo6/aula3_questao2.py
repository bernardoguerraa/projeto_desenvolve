# Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com",
# use o conceito de fatiamento de listas para criar uma lista dominios com o nome principal de todos os domínios



# Lista para armazenar as URLs
urls = []

# Loop para o usuário inserir várias URLs
while True:
    url = input("Digite uma URL (ou 'sair' para finalizar): ")
    
    if url.lower() == 'sair':
        break  # Encerra o loop se o usuário digitar 'sair'
    
    urls.append(url)  # Adiciona a URL à lista

# Cria a lista de domínios usando fatiamento
dominios = [url[4:-4] for url in urls]  # Fatiamento para remover "www." e ".com"

# Exibe a lista de domínios
print(dominios)
