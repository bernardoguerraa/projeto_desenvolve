import argparse
import os
from personalizador.layout import exibir_layout
from personalizador.painel import exibir_painel
from personalizador.progresso import exibir_progresso
from personalizador.estilo import exibir_estilo

def main():
    parser = argparse.ArgumentParser(description="Exemplo de uso do personalizador")
    parser.add_argument('texto', help="Texto ou caminho para arquivo")
    parser.add_argument('-a', '--arquivo', action='store_true', help="Indica que o texto é um caminho de arquivo")
    parser.add_argument('-m', '--modulo', required=True, choices=['layout', 'painel', 'progresso', 'estilo'], help="Escolha o módulo")
    parser.add_argument('-f', '--funcao', required=True, choices=['exibir_layout', 'exibir_painel', 'exibir_progresso', 'exibir_estilo'], help="Escolha a função do módulo")

    args = parser.parse_args()

    # Verificar se o argumento 'texto' é o caminho para um arquivo
    is_arquivo = args.arquivo

    # Chamar a função apropriada com os parâmetros corretos
    if args.modulo == 'layout' and args.funcao == 'exibir_layout':
        exibir_layout(args.texto, is_arquivo)
    elif args.modulo == 'painel' and args.funcao == 'exibir_painel':
        exibir_painel(args.texto, is_arquivo)
    elif args.modulo == 'progresso' and args.funcao == 'exibir_progresso':
        exibir_progresso(args.texto, is_arquivo)
    elif args.modulo == 'estilo' and args.funcao == 'exibir_estilo':
        exibir_estilo(args.texto, is_arquivo)

if __name__ == "__main__":
    main()

