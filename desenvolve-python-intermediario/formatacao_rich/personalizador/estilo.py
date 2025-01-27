# estilo.py

"""
Este módulo lida com funcionalidades de estilo usando a biblioteca rich.
"""

from rich.console import Console
from rich.text import Text

def exibir_estilo(texto: str, isArquivo: bool):
    """
    Exibe o texto com estilos personalizados usando o rich.

    Parâmetros:
    texto (str): O texto a ser exibido.
    isArquivo (bool): Se True, o texto será lido de um arquivo. Caso contrário, o texto é fornecido diretamente.

    Retorna:
    None
    """
    console = Console()

    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()

    # Aplicando estilos diferentes
    texto_formatado = Text(texto)
    texto_formatado.stylize("bold red")  # Aplica o estilo em negrito e vermelho

    console.print(texto_formatado)

