# painel.py

"""
Este módulo lida com funcionalidades de painel usando a biblioteca rich.
"""

from rich.console import Console
from rich.panel import Panel

def exibir_painel(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de um painel usando o rich.

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

    painel = Panel(texto, expand=False)
    console.print(painel)
