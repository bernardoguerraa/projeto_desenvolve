# layout.py

"""
Este módulo lida com funcionalidades de layout usando a biblioteca rich.
"""

from rich.console import Console
from rich.text import Text

def exibir_layout(texto: str, isArquivo: bool):
    """
    Exibe o texto em um layout formatado usando o rich.

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
    
    text = Text(texto)
    console.print(text)
