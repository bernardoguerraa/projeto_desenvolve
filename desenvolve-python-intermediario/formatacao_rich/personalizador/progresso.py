# progresso.py

"""
Este módulo lida com funcionalidades de progresso usando a biblioteca rich.
"""

from rich.console import Console
from rich.progress import Progress

def exibir_progresso(texto: str, isArquivo: bool):
    """
    Exibe o texto dentro de uma barra de progresso usando o rich.

    Parâmetros:
    texto (str): O texto a ser exibido.
    isArquivo (bool): Se True, o texto será lido de um arquivo. Caso contrário, o texto é fornecido diretamente.

    Retorna:
    None
    """
    console = Console()
    progresso = Progress()

    if isArquivo:
        with open(texto, 'r') as arquivo:
            texto = arquivo.read()
    
    tarefa = progresso.add_task("[cyan]Carregando...", total=100)

    while not progresso.finished:
        progresso.update(tarefa, advance=1)
        texto = texto + "."
        console.print(texto, style="bold green")
